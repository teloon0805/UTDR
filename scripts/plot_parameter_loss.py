"""绘制单参数教学例子的损失曲线；依赖 matplotlib，不使用训练结果。"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, findfont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/images/parameter-loss.png"
COLORS = {
    "background": "#F4F9FD",
    "ink": "#153B57",
    "muted": "#53758C",
    "curve": "#7AAAC6",
    "small_step": "#1685A8",
    "large_step": "#285FA3",
    "grid": "#DCEAF3",
    "guide": "#B9CFDF",
}


def main():
    font = findfont(FontProperties(family=[
        "Microsoft YaHei", "Noto Sans CJK SC", "WenQuanYi Zen Hei", "Arial Unicode MS"
    ]))
    plt.rcParams.update({
        "font.family": FontProperties(fname=font).get_name(),
        "font.size": 11,
        "axes.unicode_minus": False,
        "text.color": COLORS["ink"],
        "axes.labelcolor": COLORS["muted"],
        "xtick.color": COLORS["muted"],
        "ytick.color": COLORS["muted"],
    })
    values = [0.8 + index * 0.01 for index in range(441)]
    losses = [(2 * value - 6) ** 2 for value in values]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.65), sharex=True, sharey=True)
    fig.patch.set_facecolor(COLORS["background"])
    panels = [
        (axes[0], 2.5, COLORS["small_step"], "-", "o", "小步调整，损失下降", "2 → 2.5    损失 4 → 1"),
        (axes[1], 4.5, COLORS["large_step"], "--", "D", "调整过大，损失上升", "2 → 4.5    损失 4 → 9"),
    ]
    for ax, endpoint, accent, line_style, marker, title, subtitle in panels:
        ax.set_facecolor(COLORS["background"])
        ax.plot(values, losses, color=COLORS["curve"], linewidth=2.2, zorder=2)
        ax.scatter([3], [0], s=36, color=COLORS["curve"], zorder=4)
        ax.annotate("最低点 w = 3", (3, 0), xytext=(8, 36),
                    textcoords="offset points", color=COLORS["muted"], fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": COLORS["guide"], "linewidth": 0.8})
        end_loss = (2 * endpoint - 6) ** 2
        ax.scatter([2], [4], s=64, color=COLORS["ink"], zorder=5)
        ax.scatter([endpoint], [end_loss], s=76, color=accent, marker=marker, zorder=5)
        ax.annotate("起点", (2, 4), xytext=(-33, 13),
                    textcoords="offset points", color=COLORS["ink"])
        ax.annotate("调整后", (endpoint, end_loss), xytext=(12, 1),
                    textcoords="offset points", color=accent)
        ax.annotate("", xy=(endpoint, end_loss), xytext=(2, 4), arrowprops={
            "arrowstyle": "->", "color": accent, "linewidth": 2,
            "linestyle": line_style,
            "connectionstyle": "arc3,rad=-0.14", "shrinkA": 8, "shrinkB": 8,
        })
        ax.set_title(title, loc="left", fontsize=15, fontweight="bold", pad=24)
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, color=accent, fontsize=11)
        ax.set_xlabel("参数 w", labelpad=9)
        ax.set_xlim(0.8, 5.2)
        ax.set_ylim(-1, 20)
        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_yticks([0, 4, 8, 12, 16, 20])
        ax.grid(axis="y", color=COLORS["grid"], linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["bottom", "left"]].set_color(COLORS["guide"])
        ax.tick_params(length=0, pad=6)
    axes[0].set_ylabel("平方误差损失 L", labelpad=10)
    fig.text(0.055, 0.055, "教学示意 · 输入 x = 2，真实标签 y = 6；预测 ŷ = 2w，损失 L = (2w − 6)²",
             color=COLORS["muted"], fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.97, top=0.79, bottom=0.22, wspace=0.14)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=160, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    main()
