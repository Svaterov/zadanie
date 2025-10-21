from PIL import Image, ImageDraw
import random
import math

def create_generative_art(width=800, height=600, filename="./output/generative_art.png"):
    """Создает генеративное абстрактное изображение"""
    
    # Создаем новое изображение
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Генерируем 50 случайных кругов
    for _ in range(50):
        # Случайные параметры круга
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(10, 100)
        
        # Случайный цвет с прозрачностью
        color = (
            random.randint(0, 255),
            random.randint(0, 255), 
            random.randint(0, 255)
        )
        
        # Рисуем круг
        draw.ellipse(
            [x-radius, y-radius, x+radius, y+radius],
            fill=color,
            outline=None
        )
    
    # Добавляем несколько линий для структуры
    for _ in range(10):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        
        line_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        
        draw.line([x1, y1, x2, y2], fill=line_color, width=3)
    
    # Сохраняем результат
    img.save(filename, "PNG")
    print(f"Генеративное искусство сохранено как {filename}")

# Создаем 3 разных варианта
for i in range(3):
    create_generative_art(filename=f"./output/generative_art_{i+1}.png")