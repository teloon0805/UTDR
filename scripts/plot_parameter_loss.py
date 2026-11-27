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
    plot_gradient_direction(values, losses)


def plot_gradient_direction(values, losses):
    """标出两个位置的局部斜率与减小损失的更新方向。"""
    fig, ax = plt.subplots(figsize=(10.8, 4.8))
    fig.patch.set_facecolor(COLORS["background"])
    ax.set_facecolor(COLORS["background"])
    ax.plot(values, losses, color=COLORS["curve"], linewidth=2.5)

    for position, endpoint, accent, marker, label_x, title, explanation in [
        (2, 2.5, COLORS["small_step"], "o", 1.4, "梯度为负", "向右：增大参数 w"),
        (4, 3.5, COLORS["large_step"], "D", 3.45, "梯度为正", "向左：减小参数 w"),
    ]:
        loss = (2 * position - 6) ** 2
        slope = 8 * position - 24
        tangent_x = [position - 0.4, position + 0.4]
        tangent_y = [loss + slope * (value - position) for value in tangent_x]
        ax.plot(tangent_x, tangent_y, linestyle="--", color=accent, linewidth=1.8)
        ax.scatter([position], [loss], color=accent, marker=marker, s=85, zorder=5)
        ax.annotate("", xy=(endpoint, (2 * endpoint - 6) ** 2), xytext=(position, loss),
                    arrowprops={"arrowstyle": "->", "color": accent, "linewidth": 2.5,
                                "connectionstyle": "arc3,rad=0.08", "shrinkA": 8})
        ax.text(label_x, 15.5, title, fontsize=15, fontweight="bold", color=accent)
        ax.text(label_x, 13.5, explanation, fontsize=12, color=accent)

    ax.scatter([3], [0], s=42, color=COLORS["ink"], zorder=5)
    ax.annotate("本例最低点", (3, 0), xytext=(0, 28), ha="center",
                textcoords="offset points", color=COLORS["muted"],
                arrowprops={"arrowstyle": "-", "color": COLORS["guide"]})
    ax.set_title("梯度与更新方向", loc="left", fontsize=16, fontweight="bold", pad=20)
    ax.set_xlabel("参数 w（向右增大）", labelpad=8)
    ax.set_ylabel("损失 L", labelpad=10)
    ax.set_xlim(0.8, 5.2)
    ax.set_ylim(-1, 20)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([0, 4, 8, 12, 16, 20])
    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["bottom", "left"]].set_color(COLORS["guide"])
    ax.tick_params(length=0, pad=6)
    fig.text(0.065, 0.065, "虚线：当前位置的切线    箭头：减小损失的更新方向",
             color=COLORS["muted"], fontsize=10)
    fig.text(0.065, 0.02, "教学示意 · L = (2w − 6)²；图示为局部更新方向，实际更新仍需合适步长。",
             color=COLORS["muted"], fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.85, bottom=0.23)
    target = ROOT / "assets/images/gradient-direction.png"
    fig.savefig(target, dpi=160, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {target}")


if __name__ == "__main__":
    main()
