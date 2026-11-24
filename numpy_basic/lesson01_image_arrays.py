"""第 1 课：把数字数组保存成图片，再读取、裁剪和放大。"""

from pathlib import Path

import matplotlib
import numpy as np
from PIL import Image

# 只保存图，不弹出窗口，便于从终端运行。
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    output_dir = Path(__file__).resolve().parent / "outputs" / "lesson01"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. 一个数字表示一个灰度像素；这里使用 8 位无符号整数。
    gray = np.array(
        [
            [0, 64, 128, 255],
            [32, 96, 160, 224],
            [255, 192, 128, 0],
        ],
        dtype=np.uint8,
    )
    print("灰度数组：\n", gray)
    print("shape（高，宽）：", gray.shape)
    print("ndim（轴的数量）：", gray.ndim)
    print("dtype（元素的数据类型）：", gray.dtype)
    print("gray[1, 2]（第 2 行、第 3 列）：", gray[1, 2])

    # 2. 每个 RGB 像素由红、绿、蓝三个数构成。
    rgb = np.array(
        [
            [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
        ],
        dtype=np.uint8,
    )
    print("RGB shape（高，宽，通道）：", rgb.shape)
    print("rgb[0, 1] 的 RGB 数值：", rgb[0, 1])

    # 3. 保存为真实 PNG 文件，然后重新读取为数组。
    gray_path = output_dir / "gray.png"
    Image.fromarray(gray).save(gray_path)
    Image.fromarray(rgb).save(output_dir / "rgb.png")
    with Image.open(gray_path) as image:
        loaded = np.array(image)
        print("Pillow size（宽，高）：", image.size)
    print("读取前后的像素完全相同：", np.array_equal(gray, loaded))

    # 4. 裁剪：先选行，再选列；结束索引不包含在结果中。
    # .copy() 让裁剪结果独立保存，之后修改它不会影响 loaded。
    crop = loaded[0:2, 1:4].copy()
    print("裁剪后的数组：\n", crop)
    print("裁剪后的 shape：", crop.shape)
    Image.fromarray(crop).save(output_dir / "crop.png")

    # 5. resize 的尺寸顺序是（宽，高）。最近邻放大便于观察像素块。
    height, width = loaded.shape
    enlarged = Image.fromarray(loaded).resize(
        (width * 40, height * 40), resample=Image.Resampling.NEAREST
    )
    enlarged.save(output_dir / "gray_enlarged.png")
    print("放大后的 size（宽，高）：", enlarged.size)

    # 以下绘图代码用于对照观察，第一遍重点读上面的数组操作。
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, array, title in zip(
        axes,
        [gray, rgb, crop],
        ["Gray: shape=(3, 4)", "RGB: shape=(2, 3, 3)", "Crop: gray[0:2, 1:4]"],
    ):
        if array.ndim == 2:
            ax.imshow(array, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
            for row in range(array.shape[0]):
                for col in range(array.shape[1]):
                    value = int(array[row, col])
                    ax.text(
                        col, row, str(value), ha="center", va="center",
                        color="white" if value < 128 else "black", fontsize=13,
                    )
        else:
            ax.imshow(array, interpolation="nearest")
        ax.set_title(title)
        ax.set_xlabel("column index (x)")
        ax.set_ylabel("row index (y)")
        ax.set_xticks(range(array.shape[1]))
        ax.set_yticks(range(array.shape[0]))

    fig.tight_layout()
    fig.savefig(output_dir / "overview.png", dpi=160)
    plt.close(fig)
    print("图片已保存至：", output_dir)


if __name__ == "__main__":
    main()
