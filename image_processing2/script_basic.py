from PIL import Image

# Шаг 1: Открытие и сохранение

# 1. Открываем изображение
image = Image.open("./input/photo1.jpg")

# 2. Показываем информацию о изображении
print(f"Формат: {image.format}")
print(f"Размер: {image.size}") # (width, height)
print(f"Режим: {image.mode}") # RGB, L (grayscale), etc.

# 3. Сохраняем в другом формате
image.save("./output/photo1_basic.png") # Конвертация в PNG

# Шаг 2: Изменение размера и поворот

# 4. Изменяем размер (ширина 400px, высота auto)
new_size = (400, int(image.height * 400 / image.width))
resized_image = image.resize(new_size, Image.Resampling.LANCZOS)

# 5. Поворачиваем на 45 градусов
rotated_image = image.rotate(45, expand=True) # expand=True чтобы не обрезать углы

# 6. Сохраняем результаты
resized_image.save("./output/photo1_resized.jpg")
rotated_image.save("./output/photo1_rotated.jpg")

# Шаг 3: Конвертация и обрезка

# 7. Конвертируем в черно-белое
grayscale_image = image.convert("L")
grayscale_image.save("./output/photo1_bw.jpg")

# 8. Обрезаем изображение (левый_верхний_x, левый_верхний_y, правый_нижний_x, правый_нижний_y)
cropped_image = image.crop((100, 100, 400, 400)) # Квадрат 300x300
cropped_image.save("./output/photo1_cropped.jpg")

print("Все операции успешно выполнены!")