"""用第一课的灰度数组生成裁剪动图和静态图。"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT = ROOT / "assets" / "fonts" / "DMMono-Regular.ttf"
IMAGES = ROOT / "assets" / "images"
GRAY = ((0, 64, 128, 255), (32, 96, 160, 224), (255, 192, 128, 0))
CROP = tuple(row[1:4] for row in GRAY[:2])
PAPER = "#f3f2ec"
INK = "#172e32"
TEAL = "#16786b"
CELL_WIDTH = 64
CELL_HEIGHT = 48
STEP_X = 72
STEP_Y = 56


def draw_grid(draw, values, x, y, font):
    for row_index, row in enumerate(values):
        for column_index, value in enumerate(row):
            left = x + column_index * STEP_X
            top = y + row_index * STEP_Y
            draw.rounded_rectangle(
                (left, top, left + CELL_WIDTH, top + CELL_HEIGHT),
                radius=6,
                fill=(value, value, value),
                outline="#deded5",
            )
            draw.text(
                (left + CELL_WIDTH / 2, top + CELL_HEIGHT / 2),
                str(value),
                font=font,
                fill=INK if value >= 128 else "white",
                anchor="mm",
            )


def frame(progress, number_font, label_font):
    image = Image.new("RGB", (800, 294), PAPER)
    draw = ImageDraw.Draw(image)
    original_x, crop_x, grid_y = 68, 518, 91
    draw.text((original_x, 24), "Original  /  3 x 4", font=label_font, fill=INK)
    draw.text((crop_x, 24), "Crop  /  2 x 3", font=label_font, fill=INK)
    draw.line((68, 53, 726, 53), fill="#d5d9d1", width=1)

    for column in range(4):
        x = original_x + column * STEP_X + CELL_WIDTH / 2
        draw.text((x, 73), str(column), font=label_font, fill=TEAL, anchor="mm")
    for row in range(3):
        y = grid_y + row * STEP_Y + CELL_HEIGHT / 2
        draw.text((43, y), str(row), font=label_font, fill=TEAL, anchor="mm")

    draw_grid(draw, GRAY, original_x, grid_y, number_font)
    draw_grid(draw, CROP, crop_x, grid_y, number_font)
    draw.rounded_rectangle((135, 86, 353, 200), radius=10, outline=TEAL, width=3)
    draw.rounded_rectangle(
        (513, 86, 731, 200), radius=10,
        outline=TEAL if progress == 1 else "#c0cdc4", width=3,
    )
    draw.line((374, 143, 489, 143), fill="#b5c6bf", width=2)
    draw.line((481, 136, 489, 143, 481, 150), fill=TEAL, width=2)
    dot_x = round(374 + 115 * progress)
    draw.line((374, 143, dot_x, 143), fill=TEAL, width=3)
    draw.ellipse((dot_x - 4, 139, dot_x + 4, 147), fill=TEAL)
    draw.text((crop_x, 231), "gray[0:2, 1:4]", font=number_font, fill=TEAL)
    return image


def main():
    numbers = ImageFont.truetype(str(FONT), 24)
    labels = ImageFont.truetype(str(FONT), 18)
    frames = [frame(step / 24, numbers, labels) for step in range(25)]
    frames[-1].save(IMAGES / "array-crop.png", optimize=True)
    frames[0].save(
        IMAGES / "array-crop.gif",
        save_all=True,
        append_images=frames[1:],
        duration=[500] + [75] * 23 + [1100],
        optimize=True,
    )


if __name__ == "__main__":
    main()
