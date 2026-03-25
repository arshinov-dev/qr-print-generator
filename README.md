# 🖨️ QR Print Generator

[![Status](https://img.shields.io/badge/статус-Утилита-2a9d8f)](https://github.com/topics/print-tools)
[![License](https://img.shields.io/badge/лицензия-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=flat)](https://www.python.org/)
[![ReportLab](https://img.shields.io/badge/ReportLab-013243?logo=python&logoColor=white&style=flat)](https://www.reportlab.com/)
[![CairoSVG](https://img.shields.io/badge/CairoSVG-FF6B6B?logo=python&logoColor=white&style=flat)](https://cairosvg.org/)

Данный репозиторий содержит утилиту для **пакетной печати QR-кодов** на формате A4.

## О проекте

Скрипт автоматически конвертирует SVG-файлы с QR-кодами в печатный PDF-формат. 

Создан, как дополнение к проекту [PressKit](https://github.com/arshinov-dev/PressKit).

### Примечания

- **Гибкость**: настраиваемые размеры QR, отступы и качество печати
- **Обновления**: код открыт для модификации под ваши нужды

- Временные PNG-файлы хранятся в `temp_png/` (можно удалять после генерации)
- Виртуальное окружение `.venv/` создаётся один раз в корне

---

## Возможности

| Функция | Описание |
|-|-|
| Расчёт сетки A4 | Автоматическое размещение на странице |
| Настройка параметров | Размер QR, отступы, DPI через конфиг | 
| Мульти-страницы | Автоматическое создание новых страниц |

---

## Структура проекта

```bash
qr-print-generator/
├── .gitignore                    # Игнорируемые файлы Git
├── README.md                     # О проекте
├── LICENSE.md                    # Лицензия
├── requirements.txt              # Зависимости Python 
├── generate_pdf.py               # Основной скрипт генерации
├── input_svgs/                   # Папка для исходных SVG **Создайте в корне!**
├── temp_png/                     # Временные PNG (авто-создание)
├── qr_codes_print.pdf            # Итоговый файл для печати
```

---

## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/yourusername/qr-print-generator.git
```

### 2. Перейти в корень проекта

```bash
cd qr-print-generator
```

### 3. Создать виртуальное окружение

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

> ⚠️ Важно: В requirements.txt может потребоваться добавить cairosvg и Pillow, если они отсутствуют.

---

## Использование 

### 1. Подготовить SVG-файлы

Создайте папку с названием ```input_svgs``` в корне проекта

Поместите ваши QR-коды в формате SVG в папку ```input_svgs/:```

### 2. Настроить параметры (опционально)

```python
QR_WIDTH_MM = 20      # Ширина QR на бумаге (мм)
QR_HEIGHT_MM = 20     # Высота QR на бумаге (мм)
DPI = 300             # Качество печати
MARGIN_MM = 10        # Отступ от края листа
GAP_MM = 5            # Расстояние между кодами
```

### 3. Запустить генерацию

```bash
python generate_pdf.py
```

### 4. Получить результат

Готовый файл ```qr_codes_print.pdf``` появится в корне проекта.

## Технические детали

| Параметр | Значение |
|-|-|
| Формат бумаги | A4 (210 × 297 мм) |
| Качество печат | 300 DPI |
| Размер QR (по умолчанию) | 20 × 20 мм |
| Отступы (по умолчанию) | 10 мм от края |
| Расстояние между QR | 5 мм |

> 📊 Вместимость страницы: при стандартных настройках ~6×9 = 54 QR-кода на лист

---

## Лицензия

Данный проект лицензирован под [MIT License](LICENSE).

Это означает, что вы можете свободно использовать, изменять и распространять код.

> ***При условии сохранения уведомления об авторских правах.***

---

## Контакты

| Автор | Никнейм |
|:-:|:-:|
| Arshinov Maxim | [@arshinov-dev](https://github.com/arshinov-dev)|

> Взаимосвязанный проект: <https://github.com/arshinov-dev/PressKit>

> Весь инструментарий: <https://github.com/topics/arh-tools>

---

<p align="center">
  <img src="https://github.com/arushinofu/git-learning/blob/main/assets/images/avatar.png" alt="Логотип" width="85">
</p>

<p align="center">© arshinov.su 2026</p>

<div align="center">

[⬆️ Наверх](#-QR)

</div>
