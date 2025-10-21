from PIL import Image, ImageFilter
import os

def create_collage(image_paths, output_path, collage_size=(1200, 800)):
    """Создает коллаж из нескольких изображений"""
    
    # Проверяем, что есть изображения для коллажа
    if not image_paths:
        print("❌ Нет изображений для создания коллажа")
        return
    
    collage = Image.new('RGB', collage_size, 'white')
    draw = ImageDraw.Draw(collage)
    
    # Если изображений мало, располагаем их в ряд
    if len(image_paths) <= 3:
        x_offset = 0
        max_height = 0
        
        for img_path in image_paths:
            with Image.open(img_path) as img:
                # Ресайзим изображения для коллажа
                img.thumbnail((400, 400))
                collage.paste(img, (x_offset, (collage_size[1] - img.height) // 2))
                x_offset += img.width
                max_height = max(max_height, img.height)
                
    else:
        # Для большего количества изображений - сетка 2x2
        positions = [
            (0, 0),
            (collage_size[0] // 2, 0),
            (0, collage_size[1] // 2),
            (collage_size[0] // 2, collage_size[1] // 2)
        ]
        
        for i, img_path in enumerate(image_paths[:4]):  # Берем первые 4 изображения
            with Image.open(img_path) as img:
                img.thumbnail((collage_size[0] // 2, collage_size[1] // 2))
                collage.paste(img, positions[i])
    
    # Добавляем заголовок
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()
    
    draw.text((20, 20), "Мой коллаж", fill="black", font=font)
    
    collage.save(output_path)
    print(f"✅ Коллаж сохранен: {output_path}")

def apply_filters(image_path, output_path):
    """Применяет различные фильтры к изображению"""
    
    try:
        with Image.open(image_path) as img:
            # Размытие
            blurred = img.filter(ImageFilter.GaussianBlur(5))
            blurred.save(output_path.replace('.jpg', '_blurred.jpg'))
            print(f"✅ Размытие: {os.path.basename(output_path.replace('.jpg', '_blurred.jpg'))}")
            
            # Контур
            edges = img.filter(ImageFilter.FIND_EDGES)
            edges.save(output_path.replace('.jpg', '_edges.jpg'))
            print(f"✅ Контуры: {os.path.basename(output_path.replace('.jpg', '_edges.jpg'))}")
            
            # Ч/Б
            bw = img.convert('L')
            bw.save(output_path.replace('.jpg', '_bw.jpg'))
            print(f"✅ Ч/Б: {os.path.basename(output_path.replace('.jpg', '_bw.jpg'))}")
            
            # Дополнительные фильтры
            # Резкость
            sharpened = img.filter(ImageFilter.SHARPEN)
            sharpened.save(output_path.replace('.jpg', '_sharpened.jpg'))
            print(f"✅ Резкость: {os.path.basename(output_path.replace('.jpg', '_sharpened.jpg'))}")
            
            # Детализация
            detail = img.filter(ImageFilter.DETAIL)
            detail.save(output_path.replace('.jpg', '_detail.jpg'))
            print(f"✅ Детали: {os.path.basename(output_path.replace('.jpg', '_detail.jpg'))}")
            
    except Exception as e:
        print(f"❌ Ошибка при применении фильтров к {image_path}: {e}")

def main():
    """Основная функция для продвинутых операций"""
    print("=== ПРОДВИНУТЫЕ ОПЕРАЦИИ С ИЗОБРАЖЕНИЯМИ ===")
    
    # Создаем папку output если её нет
    os.makedirs("./output", exist_ok=True)
    
    # Получаем список изображений из папки input
    input_files = []
    supported_formats = ('.jpg', '.jpeg', '.png', '.webp')
    
    for filename in os.listdir("./input"):
        if filename.lower().endswith(supported_formats):
            input_files.append(os.path.join("./input", filename))
    
    if not input_files:
        print("❌ В папке 'input' нет изображений")
        return
    
    print(f"📁 Найдено изображений: {len(input_files)}")
    
    # Задача 1: Создание коллажа
    print("\n🎨 СОЗДАНИЕ КОЛЛАЖА")
    create_collage(input_files, "./output/collage.jpg")
    
    # Задача 2: Применение фильтров к первому изображению
    print("\n🔮 ПРИМЕНЕНИЕ ФИЛЬТРОВ")
    if input_files:
        apply_filters(input_files[0], "./output/filtered_image.jpg")
    
    # Дополнительно: применяем фильтры ко всем изображениям
    print("\n🔮 ПАКЕТНОЕ ПРИМЕНЕНИЕ ФИЛЬТРОВ")
    for i, img_path in enumerate(input_files[:2]):  # Обрабатываем первые 2 изображения
        print(f"\nОбработка: {os.path.basename(img_path)}")
        apply_filters(img_path, f"./output/filtered_{i+1}.jpg")
    
    print("\n🎉 Все продвинутые операции завершены!")

if __name__ == "__main__":
    # Нужно импортировать ImageDraw для работы с текстом
    from PIL import ImageDraw, ImageFont
    main()