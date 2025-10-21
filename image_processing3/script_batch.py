from PIL import Image, ImageDraw, ImageFont
import os

def process_image(input_path, output_path, watermark_text="@developer"):
    """Обрабатывает одно изображение: ресайз + водяной знак"""
    
    with Image.open(input_path) as img:
        # Создаем копию для работы
        working_img = img.copy()
        
        # Ресайз до ширины 800px
        if working_img.width > 800:
            new_height = int((800 / working_img.width) * working_img.height)
            working_img = working_img.resize((800, new_height), Image.Resampling.LANCZOS)
        
        # Добавляем водяной знак
        draw = ImageDraw.Draw(working_img)
        
        try:
            # Пробуем использовать системный шрифт
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            # Если шрифт не найден, используем стандартный
            font = ImageFont.load_default()
        
        # Получаем размеры текста
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Позиция в правом нижнем углу с отступом
        margin = 10
        x = working_img.width - text_width - margin
        y = working_img.height - text_height - margin
        
        # Рисуем текст с черной обводкой для читаемости
        draw.text((x-1, y-1), watermark_text, font=font, fill="black")
        draw.text((x+1, y-1), watermark_text, font=font, fill="black")
        draw.text((x-1, y+1), watermark_text, font=font, fill="black")
        draw.text((x+1, y+1), watermark_text, font=font, fill="black")
        draw.text((x, y), watermark_text, font=font, fill="white")
        
        # Сохраняем результат
        working_img.save(output_path, "JPEG", quality=85)
        print(f"Обработано: {os.path.basename(input_path)}")

def process_folder(input_folder, output_folder, watermark_text):
    """Обрабатывает все изображения в папке"""
    
    # Создаем папку output если её нет
    os.makedirs(output_folder, exist_ok=True)
    
    # Поддерживаемые форматы
    supported_formats = ('.jpg', '.jpeg', '.png', '.webp')
    
    # Обрабатываем каждый файл
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_folder, filename)
            
            # Создаем новое имя файла
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}_processed.jpg"
            output_path = os.path.join(output_folder, output_filename)
            
            # Обрабатываем изображение
            process_image(input_path, output_path, watermark_text)

# Запускаем обработку
if __name__ == "__main__":
    process_folder("./input", "./output", "© Developer Team 2024")
    print("Пакетная обработка завершена!")