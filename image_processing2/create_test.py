from PIL import Image, ImageDraw
import os

# Создаем папку input если её нет
if not os.path.exists('input'):
    os.makedirs('input')

# Создаем тестовое изображение 1
img1 = Image.new('RGB', (800, 600), color='lightblue')
draw = ImageDraw.Draw(img1)
draw.rectangle([100, 100, 400, 400], fill='red', outline='black')
draw.ellipse([500, 200, 700, 400], fill='green', outline='black')
draw.text((150, 500), "Тест Photo 1", fill='black')
img1.save('input/photo1.jpg')

# Создаем тестовое изображение 2
img2 = Image.new('RGB', (800, 600), color='lightyellow')
draw = ImageDraw.Draw(img2)
draw.polygon([(400, 100), (200, 500), (600, 500)], fill='blue')
draw.text((300, 550), "Тест Photo 2", fill='black')
img2.save('input/photo2.jpg')

print("✅ Созданы тестовые изображения в папке 'input'")