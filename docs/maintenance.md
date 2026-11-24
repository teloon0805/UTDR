# 怎样持续更新

[← 返回首页](../README.md)

## 新增一天的记录

在项目根目录打开终端：

```powershell
python scripts/new_entry.py --topic "今天的问题"
```

脚本只使用 Python 标准库，默认按北京时间创建 `journal/年份/YYYY-MM-DD.md`。已经有当天记录时，会提示编辑现有文件，保护原内容。

想明确指定日期，可以使用下面的形式；将示例日期改为实际学习日期：

```powershell
python scripts/new_entry.py --date 2026-11-25 --topic "训练集、验证集与测试集"
```

可以先查看将创建的路径：

```powershell
python scripts/new_entry.py --date 2026-11-25 --topic "训练集、验证集与测试集" --preview
```

## 整理完成后刷新

填写记录里的五个部分。整理好后，将文件顶部的 `status: draft` 改为 `status: recorded`，再执行：

```powershell
python scripts/new_entry.py --refresh
```

脚本自动更新日志目录、首页最近三篇记录，以及首页的记录数量与日期。`recorded` 表示笔记已成文，不表示完成了整个主题的学习。草稿会单独标注。

首页两组 `LEARNING` 注释之间的内容和日志索引由脚本维护；其他正文可以直接编辑。

## 增加图片与成果

1. 学习图示放在 `assets/images/`，在记录里补充文字说明和来源。
2. 实验结果按[成果模板](../templates/result.md)写在 `showcase/`，注明数据、设置、指标和运行方式。
3. 在[成果档案](../showcase/README.md)与首页最后的成果区添加链接。

示例数据和真实实验结果要分别说明。原始数据通常通过来源链接获取，是否可重新分发以数据许可为准。

## 提交到 GitHub

先查看本次修改，再按实际修改的文件暂存、提交。例如只更新一篇日志和索引时：

```powershell
git status
git diff
git add README.md journal
git commit -m "docs: record today's learning"
git push origin main
```

同时修改图片或成果档案时，将相应目录加入本次暂存范围。

## 图片维护

裁剪动图和静态图由 `scripts/build_visuals.py` 生成，使用 Pillow 和仓库里附有许可的 DM Mono 字体。

```powershell
python scripts/build_visuals.py
```

封面摄影署名和图片来源见[素材说明](design.md)。
