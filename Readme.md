# Books Scraper — books.toscrape.com

Парсер книг с сайта [books.toscrape.com](https://books.toscrape.com) на основе Selenium. Собирает данные о названии, цене и рейтинге книг по всем страницам каталога и сохраняет результаты в CSV и Excel.

## Возможности

- Обход всех страниц каталога (до `MAX_PAGES` страниц)
- Сбор данных: название, цена (£), рейтинг (1–5)
- Сохранение в `CSV` и `Excel` (два листа: все книги + статистика по рейтингу)
- Поддержка headless-режима (без открытия браузера)
- Автоматическая загрузка ChromeDriver через `webdriver-manager`

## Структура проекта

```
mini-project_selenium/
├── config.py         # Настройки: URL, таймауты, пути к файлам, headless
├── driver_setup.py   # Инициализация Chrome WebDriver
├── parser.py         # Парсинг карточек книг и навигация по страницам
├── saver.py          # Сохранение в CSV и Excel
├── scrapper.py       # Точка входа: оркестрация сбора данных
├── data/             # Папка для выходных файлов
│   ├── books_data.csv
│   └── books_data.xlsx
└── requirements.txt
```

## Установка

```bash
# Клонировать репозиторий
git clone <repo-url>
cd mini-project_selenium

# Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt
```

> Требуется Google Chrome. ChromeDriver загружается автоматически.

## Запуск

```bash
python scrapper.py
```

После выполнения в папке `data/` появятся файлы `books_data.csv` и `books_data.xlsx`.

## Конфигурация

Все параметры задаются в `config.py`:

| Параметр    | По умолчанию                      | Описание                              |
|-------------|-----------------------------------|---------------------------------------|
| `START_URL` | `https://books.toscrape.com/`     | Начальный URL                         |
| `TIMEOUT`   | `15`                              | Время ожидания элементов (сек)        |
| `MAX_PAGES` | `50`                              | Максимальное количество страниц       |
| `CSV_FILE`  | `data/books_data.csv`             | Путь к CSV-файлу                      |
| `EXCEL_FILE`| `data/books_data.xlsx`            | Путь к Excel-файлу                    |
| `HEADLESS`  | `False`                           | `True` — запуск без открытия браузера |

## Выходные данные

**CSV** (`books_data.csv`) — плоский список всех книг:

| title | price | rating |
|-------|-------|--------|
| A Light in the Attic | 51.77 | 3 |

**Excel** (`books_data.xlsx`) — два листа:
- `Все книги` — полный список
- `По рейтингу` — сводная статистика (количество, средняя/мин/макс цена)

## Зависимости

- `selenium` — управление браузером
- `webdriver-manager` — автозагрузка ChromeDriver
- `pandas` + `openpyxl` — формирование Excel-отчёта
