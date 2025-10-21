from PIL import Image
import os

def basic_operations():
    print("=== БАЗОВЫЕ ОПЕРАЦИИ С ИЗОБРАЖЕНИЯМИ ===")
    
    # Проверяем папку input
    if not os.path.exists('input'):
        print("❌ Папка 'input' не найдена!")
        return
    
    files = os.listdir('input')
    print(f"📁 Файлов в папке input: {len(files)}")
    
    if not files:
        print("⚠️  Добавьте JPEG фото в папку 'input'!")
        return
    
    # Обрабатываем каждый файл
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            print(f"\n🔄 Обрабатываем: {filename}")
            
            try:
                # Открываем изображение
                input_path = os.path.join('input', filename)
                with Image.open(input_path) as img:
                    # Выводим информацию
                    print(f"   📐 Размер: {img.size}")
                    print(f"   🎨 Режим: {img.mode}")
                    print(f"   📄 Формат: {img.format}")
                    
                    # Создаем миниатюру
                    img.thumbnail((300, 300))
                    
                    # Сохраняем
                    output_name = f"thumb_{filename}"
                    output_path = os.path.join('output', output_name)
                    img.save(output_path)
                    print(f"   ✅ Сохранено: {output_name}")
                    
            except Exception as e:
                print(f"   ❌ Ошибка: {e}")

if __name__ == "__main__":
    basic_operations()