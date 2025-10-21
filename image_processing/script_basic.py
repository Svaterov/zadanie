from PIL import Image
import os

def basic_operations():
    """Базовые операции с одним изображением"""
    print("=== БАЗОВЫЕ ОПЕРАЦИИ С ИЗОБРАЖЕНИЯМИ ===")
    
    # Создаем папку output если её нет
    os.makedirs("./output", exist_ok=True)
    
    try:
        # Шаг 1: Открытие и сохранение
        print("\n1. 📂 ОТКРЫТИЕ И СОХРАНЕНИЕ")
        
        # 1. Открываем изображение
        image = Image.open("./input/photo1.jpg")
        
        # 2. Показываем информацию о изображении
        print(f"   Формат: {image.format}")
        print(f"   Размер: {image.size}")  # (width, height)
        print(f"   Режим: {image.mode}")   # RGB, L (grayscale), etc.
        
        # 3. Сохраняем в другом формате
        image.save("./output/photo1_basic.png")  # Конвертация в PNG
        print("   ✅ Сохранено как PNG: photo1_basic.png")
        
        # Шаг 2: Изменение размера и поворот
        print("\n2. 📏 ИЗМЕНЕНИЕ РАЗМЕРА И ПОВОРОТ")
        
        # 4. Изменяем размер (ширина 400px, высота auto)
        new_size = (400, int(image.height * 400 / image.width))
        resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
        print(f"   Новый размер: {new_size}")
        
        # 5. Поворачиваем на 45 градусов
        rotated_image = image.rotate(45, expand=True)  # expand=True чтобы не обрезать углы
        
        # 6. Сохраняем результаты
        resized_image.save("./output/photo1_resized.jpg")
        rotated_image.save("./output/photo1_rotated.jpg")
        print("   ✅ Сохранено: photo1_resized.jpg")
        print("   ✅ Сохранено: photo1_rotated.jpg")
        
        # Шаг 3: Конвертация и обрезка
        print("\n3. 🎨 КОНВЕРТАЦИЯ И ОБРЕЗКА")
        
        # 7. Конвертируем в черно-белое
        grayscale_image = image.convert("L")
        grayscale_image.save("./output/photo1_bw.jpg")
        print("   ✅ Чёрно-белое: photo1_bw.jpg")
        
        # 8. Обрезаем изображение
        cropped_image = image.crop((100, 100, 400, 400))  # Квадрат 300x300
        cropped_image.save("./output/photo1_cropped.jpg")
        print("   ✅ Обрезанное: photo1_cropped.jpg")
        
        print(f"\n🎉 ВСЕ ОПЕРАЦИИ УСПЕШНО ВЫПОЛНЕНЫ!")
        print("📁 Результаты сохранены в папке 'output'")
        
    except FileNotFoundError:
        print("❌ ОШИБКА: Файл './input/photo1.jpg' не найден!")
        print("   Убедитесь, что:")
        print("   - Папка 'input' существует")
        print("   - В папке 'input' есть файл 'photo1.jpg'")
        print("   - Файл имеет правильное расширение (.jpg или .jpeg)")

if __name__ == "__main__":
    basic_operations()