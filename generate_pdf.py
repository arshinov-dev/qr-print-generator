import os
import glob
import cairosvg
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from PIL import Image

# --- НАСТРОЙКИ ---
INPUT_FOLDER = "input_svgs"       # Папка с исходными SVG
TEMP_FOLDER = "temp_png"          # Папка для временных PNG
OUTPUT_FILE = "qr_codes_print.pdf"

QR_WIDTH_MM = 20                  # Ширина блока с QR на бумаге (мм)
QR_HEIGHT_MM = 20                 # Высота блока с QR на бумаге (мм)
DPI = 300                         # Качество печати (300 - стандарт)
MARGIN_MM = 10                    # Отступ от края листа
GAP_MM = 5                        # Расстояние между кодами

# --- КОНСТАНТЫ ---
A4_WIDTH_MM = 210
A4_HEIGHT_MM = 297

def mm_to_px(mm_val, dpi):
    """Перевод мм в пиксели для заданного DPI"""
    return int((mm_val / 25.4) * dpi)

def mm_to_pt(mm_val):
    """Перевод мм в пункты для PDF (1 pt = 1/72 inch)"""
    return mm_val * 72 / 25.4

def main():
    # 1. Подготовка папок
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        print(f"Создана папка {INPUT_FOLDER}. Положите туда SVG и запустите снова.")
        return
    
    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)

    svg_files = sorted(glob.glob(os.path.join(INPUT_FOLDER, "*.svg")))
    svg_files += sorted(glob.glob(os.path.join(INPUT_FOLDER, "*.SVG")))
    svg_files = sorted(list(set(svg_files)))

    if not svg_files:
        print("SVG файлы не найдены!")
        return

    print(f"Найдено SVG: {len(svg_files)}")

    # 2. Конвертация SVG -> PNG
    # Считаем размер в пикселях для целевого размера 30x33 мм
    png_width_px = mm_to_px(QR_WIDTH_MM, DPI)
    png_height_px = mm_to_px(QR_HEIGHT_MM, DPI)
    
    png_files = []
    print("Конвертация SVG в PNG...")
    
    for i, svg_path in enumerate(svg_files):
        filename = os.path.basename(svg_path)
        png_name = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(TEMP_FOLDER, png_name)
        
        try:
            # Конвертируем с фиксированными output_width/output_height
            cairosvg.svg2png(
                url=svg_path, 
                write_to=png_path,
                output_width=png_width_px,
                output_height=png_height_px,
                dpi=DPI
            )
            png_files.append(png_path)
        except Exception as e:
            print(f"Ошибка конвертации {filename}: {e}")
    
    print(f"Конвертировано: {len(png_files)}")

    # 3. Расчет сетки
    usable_width = A4_WIDTH_MM - (2 * MARGIN_MM)
    usable_height = A4_HEIGHT_MM - (2 * MARGIN_MM)

    cell_width = QR_WIDTH_MM + GAP_MM
    cell_height = QR_HEIGHT_MM + GAP_MM

    cols = int(usable_width // cell_width)
    rows = int(usable_height // cell_height)

    if cols < 1 or rows < 1:
        print("Ошибка: QR слишком большой для заданных отступов")
        return

    items_per_page = cols * rows
    print(f"Вместимость страницы: {items_per_page} шт. ({cols}x{rows})")

    # 4. Генерация PDF
    c = canvas.Canvas(OUTPUT_FILE, pagesize=A4)
    
    start_x_pt = mm_to_pt(MARGIN_MM)
    # Начинаем с верхнего ряда: y — это нижняя граница картинки (anchor='sw')
    start_y_top_pt = mm_to_pt(A4_HEIGHT_MM - MARGIN_MM - QR_HEIGHT_MM)
    width_pt = mm_to_pt(QR_WIDTH_MM)
    height_pt = mm_to_pt(QR_HEIGHT_MM)

    current_index = 0
    total = len(png_files)

    while current_index < total:
        # Новая страница (кроме самой первой итерации, если мы только начали)
        if current_index > 0 and current_index % items_per_page == 0:
            c.showPage()
        
        for row in range(rows):
            for col in range(cols):
                if current_index >= total:
                    break
                
                img_path = png_files[current_index]
                print(f"Добавление: {os.path.basename(img_path)} ({current_index + 1}/{total})")

                x = start_x_pt + (col * mm_to_pt(cell_width))
                y = start_y_top_pt - (row * mm_to_pt(cell_height))

                # Вставляем картинку. 
                # anchor='sw' означает, что координаты (x,y) задают Нижний-Левый угол
                c.drawImage(
                    img_path,
                    x,
                    y,
                    width=width_pt,
                    height=height_pt,
                    anchor='sw',
                    preserveAspectRatio=False
                )
                
                current_index += 1

    c.save()
    print(f"\nГОТОВО! Файл: {OUTPUT_FILE}")
    print("Можете удалять папку temp_png, если нужно")

if __name__ == "__main__":
    main()
