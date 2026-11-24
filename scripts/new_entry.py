"""创建学习记录，并同步 README 中的日志索引。只使用 Python 标准库。"""

import argparse
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BEIJING = timezone(timedelta(hours=8))


def iso_date(value):
    try:
        parsed = date.fromisoformat(value)
        if parsed.isoformat() != value:
            raise ValueError
        return parsed
    except ValueError as error:
        raise argparse.ArgumentTypeError("日期请使用 YYYY-MM-DD 格式。") from error


def table_text(value):
    return value.replace("|", "&#124;").replace("[", "&#91;").replace("]", "&#93;")


def entries(root):
    result = []
    for path in sorted((root / "journal").glob("[0-9]*/????-??-??.md"), reverse=True):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---", text, re.DOTALL)
        if not match:
            raise ValueError(f"记录缺少顶部信息：{path}")
        metadata = dict(
            line.split(":", 1) for line in match.group(1).splitlines() if ":" in line
        )
        metadata = {key.strip(): value.strip() for key, value in metadata.items()}
        if metadata.get("status") not in {"draft", "recorded"}:
            raise ValueError(f"记录状态须为 draft 或 recorded：{path}")
        entry_date = iso_date(metadata.get("date", ""))
        if path.stem != entry_date.isoformat() or path.parent.name != str(entry_date.year):
            raise ValueError(f"记录日期与路径不一致：{path}")
        title = metadata.get("title", "").strip()
        if not title:
            raise ValueError(f"记录缺少标题：{path}")
        result.append({"path": path, "date": entry_date, "title": title,
                       "status": metadata["status"]})
    return result


def replace_section(text, name, content):
    start = f"<!-- LEARNING:{name}:START -->"
    end = f"<!-- LEARNING:{name}:END -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"索引标记 {name} 缺失或重复；未改写文件。")
    before, tail = text.split(start, 1)
    middle, after = tail.split(end, 1)
    if end in before or start in after:
        raise ValueError(f"索引标记 {name} 的顺序不正确。")
    return before + start + "\n" + content + "\n" + end + after


def index_table(records, base):
    lines = ["| 日期 | 学习主题 | 记录状态 |", "| --- | --- | --- |"]
    for entry in records:
        relative = entry["path"].relative_to(base).as_posix()
        status = "已整理" if entry["status"] == "recorded" else "草稿 · 待补充"
        lines.append(f"| {entry['date']} | [{table_text(entry['title'])}]({relative}) | {status} |")
    if not records:
        lines.append("| — | 等待第一篇记录 | — |")
    return "\n".join(lines)


def refresh(root=ROOT):
    records = entries(root)
    recorded = sum(entry["status"] == "recorded" for entry in records)
    drafts = len(records) - recorded
    latest = f"最近记录 {records[0]['date']} · " if records else ""
    draft_count = f" · {drafts} 篇草稿" if drafts else ""
    summary = f"*{latest}{recorded} 篇笔记{draft_count}*"
    recent = []
    for entry in records[:3]:
        path = entry["path"].relative_to(root).as_posix()
        status = "（草稿）" if entry["status"] == "draft" else ""
        recent.append(f"- {entry['date']} · [{table_text(entry['title'])}]({path}){status}")
    homepage = root / "README.md"
    journal = root / "journal" / "README.md"
    home_text = replace_section(homepage.read_text(encoding="utf-8"), "SUMMARY", summary)
    home_text = replace_section(home_text, "RECENT", "\n".join(recent) or "等待第一篇记录。")
    journal_text = replace_section(
        journal.read_text(encoding="utf-8"), "INDEX", index_table(records, root / "journal")
    )
    # 先核对两个文件的标记，再写入；其余手写内容保持原样。
    homepage.write_text(home_text, encoding="utf-8")
    journal.write_text(journal_text, encoding="utf-8")
    print(f"索引已更新：{recorded} 篇已整理记录，{drafts} 篇草稿。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", help="今天学习的问题或主题")
    parser.add_argument("--date", type=iso_date, default=datetime.now(BEIJING).date())
    parser.add_argument("--refresh", action="store_true", help="只更新记录索引")
    parser.add_argument("--preview", action="store_true", help="只查看新文件路径")
    args = parser.parse_args()
    if args.refresh:
        if args.preview or args.topic:
            parser.error("--refresh 请单独使用。")
        refresh()
        return
    if not args.topic or not args.topic.strip():
        parser.error("请用 --topic 填写今天的问题。")
    if "\n" in args.topic or "\r" in args.topic:
        parser.error("主题请写在一行内。")
    target = ROOT / "journal" / str(args.date.year) / f"{args.date.isoformat()}.md"
    if target.exists():
        parser.exit(1, f"当天记录已存在，请直接编辑；原文件保持不变：\n{target}\n")
    if args.preview:
        print("将创建：", target)
        return
    # 先检查现有索引，避免在错误的仓库结构中创建记录。
    entries(ROOT)
    replace_section((ROOT / "README.md").read_text(encoding="utf-8"), "SUMMARY", "")
    replace_section((ROOT / "README.md").read_text(encoding="utf-8"), "RECENT", "")
    replace_section((ROOT / "journal" / "README.md").read_text(encoding="utf-8"), "INDEX", "")
    template = (ROOT / "templates" / "daily.md").read_text(encoding="utf-8")
    content = template.replace("{{date}}", args.date.isoformat()).replace("{{topic}}", args.topic.strip())
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("x", encoding="utf-8") as file:
        file.write(content)
    refresh()
    print("已创建学习草稿：", target)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, argparse.ArgumentTypeError) as error:
        raise SystemExit(str(error)) from error
