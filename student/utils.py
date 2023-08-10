# captcha/utils.py
import random
from PIL import Image, ImageDraw, ImageFont

import sys
print(sys.executable)

def generate_captcha():
    width, height = 200, 80
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Generate a random 6-character CAPTCHA text
    captcha_text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

    font = ImageFont.truetype('D:\VSCODE PROGRAMS\Studash\pro\Fonts\SpecialElite-Regular.ttf', 40)
    text_width, text_height = draw.textsize(captcha_text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    draw.text((x, y), captcha_text, font=font, fill=(0, 0, 0))

    return image, captcha_text
