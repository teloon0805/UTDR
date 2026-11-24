"""生成 README 封面与泛化教学图；图中的分数来自例题，不是实验结果。"""

from pathlib import Path
import math
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "outputs" / ".matplotlib"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONTS = ROOT / "assets" / "fonts"
IMAGES = ROOT / "assets" / "images"
NAVY = "#0a2430"
TEAL = "#40d5bd"
PAPER = "#f5f8f7"


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def cover():
    image = Image.new("RGB", (1600, 560), NAVY)
    draw = ImageDraw.Draw(image)
    # 原创的海流等高线；不表示任何测量数据。
    for row in range(20):
        for col in range(23):
            x, y = 910 + col * 28, 30 + row * 27
            draw.ellipse((x, y, x + 2, y + 2), fill="#20444d")
    for line in range(29):
        points = []
        for step in range(180):
            x = 892 + step * 4.4
            y = 90 + line * 13 + 47 * math.sin((x - 920) / 170 + line * 0.045)
            y += 18 * math.cos((x - 950) / 105)
            points.append((x, y))
        draw.line(points, fill="#2d8d8a" if line % 5 == 0 else "#1c545f", width=2)
    draw.line((82, 72, 126, 72), fill=TEAL, width=4)
    draw.text((145, 58), "PERSONAL LEARNING JOURNAL", font=font("DMMono-Regular.ttf", 20), fill=TEAL)
    draw.text((74, 104), "UTDR", font=font("BricolageGrotesque-Bold.ttf", 166), fill=PAPER)
    draw.text((84, 309), "Learning, one clear idea at a time.",
              font=font("CrimsonPro-Italic.ttf", 46), fill="#d3e7e5")
    draw.text((87, 399), "UNDERWATER PERCEPTION & MACHINE LEARNING",
              font=font("DMMono-Regular.ttf", 19), fill="#90b4b8")
    draw.line((86, 464, 814, 464), fill="#2c505c", width=1)
    draw.text((87, 489), "THEORY  /  NOTES  /  EXPERIMENTS  /  REFLECTIONS",
              font=font("DMMono-Regular.ttf", 16), fill="#9cbec1")
    draw.text((1080, 489), "START WITH QUESTIONS.",
              font=font("DMMono-Regular.ttf", 17), fill=TEAL)
    image.save(IMAGES / "cover.png", optimize=True)


def chinese_font():
    candidates = [
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/System/Library/Fonts/PingFang.ttc"),
    ]
    return next((path for path in candidates if path.exists()), None)


def generalization():
    cjk = chinese_font()
    regular = FontProperties(fname=str(cjk or FONTS / "BricolageGrotesque-Bold.ttf"))
    mono = FontProperties(fname=str(FONTS / "DMMono-Regular.ttf"))
    words = {
        "title": "看见泛化：训练与验证",
        "tag": "教学示例 / 非实际训练结果",
        "train": "训练准确率",
        "validation": "验证准确率",
        "model_a": "模型 A",
        "model_b": "模型 B",
        "focus": "同一评价条件下",
        "choice": "优先考虑 B",
        "detail": "B 的验证准确率更高\n对新样本的判断更有依据",
        "foot": "数据来自学习例题；一次验证结果不代表在任意环境下都有效。",
    }
    if not cjk:
        words = {
            "title": "Understanding generalization",
            "tag": "TEACHING EXAMPLE / NOT EXPERIMENTAL RESULTS",
            "train": "Training accuracy", "validation": "Validation accuracy",
            "model_a": "Model A", "model_b": "Model B",
            "focus": "Same evaluation setup", "choice": "Prefer model B",
            "detail": "Higher validation accuracy\nBetter evidence on unseen data",
            "foot": "Illustrative scores only. One validation result does not establish performance everywhere.",
        }
    fig = plt.figure(figsize=(12.5, 5.4), facecolor=PAPER)
    fig.text(0.07, 0.85, words["title"], fontproperties=regular, fontsize=24, color=NAVY)
    fig.text(0.07, 0.94, "LEARNING NOTE / 2026.11.24", fontproperties=mono, fontsize=10, color="#50817e")
    fig.text(0.07, 0.77, words["tag"], fontproperties=regular, fontsize=10, color="#82633a")
    ax = fig.add_axes((0.12, 0.23, 0.55, 0.45), facecolor=PAPER)
    positions = np.array([1.0, 0.0])
    training = [99, 91]
    validation = [72, 87]
    ax.barh(positions + 0.15, training, height=0.25, color="#bdcbd0", label=words["train"])
    ax.barh(positions - 0.15, validation, height=0.25, color="#168d80", label=words["validation"])
    for ys, values, color in [(positions + 0.15, training, "#53656c"),
                               (positions - 0.15, validation, "#116d64")]:
        for y, value in zip(ys, values):
            ax.text(value + 1.3, y, f"{value}%", va="center", fontsize=12,
                    fontproperties=mono, color=color)
    ax.set_yticks(positions, [words["model_a"], words["model_b"]], fontproperties=regular, fontsize=13)
    ax.set_xticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"], fontproperties=mono)
    ax.set_xlim(0, 110)
    ax.set_ylim(-0.55, 1.55)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color="#dce5e5", linewidth=0.7)
    ax.tick_params(axis="both", length=0, pad=10, colors="#547076")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.legend(loc="lower left", bbox_to_anchor=(0, -0.30), ncol=2,
              frameon=False, prop=regular, labelcolor=NAVY)
    box = FancyBboxPatch((0.735, 0.26), 0.205, 0.39, boxstyle="round,pad=0.018,rounding_size=0.02",
                         transform=fig.transFigure, facecolor="#e3f0eb", edgecolor="none")
    fig.add_artist(box)
    fig.text(0.755, 0.57, words["focus"], fontproperties=regular, fontsize=11, color="#527b70")
    fig.text(0.755, 0.47, words["choice"], fontproperties=regular, fontsize=20, color="#146b60")
    fig.text(0.755, 0.34, words["detail"], fontproperties=regular, fontsize=10,
             color="#416f65", linespacing=1.8)
    fig.text(0.07, 0.045, words["foot"], fontproperties=regular, fontsize=10, color="#637c80")
    fig.savefig(IMAGES / "generalization.png", dpi=160, facecolor=PAPER)
    plt.close(fig)


if __name__ == "__main__":
    IMAGES.mkdir(parents=True, exist_ok=True)
    cover()
    generalization()
    print("已生成封面与泛化概念图：", IMAGES)
