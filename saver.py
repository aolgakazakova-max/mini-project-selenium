import csv
import logging
import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment
from config import CSV_FILE, EXCEL_FILE


logger = logging.getLogger(__name__)


def save_to_csv(books: list[dict], filename: str = CSV_FILE):
    if not books:
        logger.warning('Список книг пуст - CSV не создан')
        return

    fieldnames = ['title', 'price', 'rating']

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
    logger.info(f'CSV: сохранено {len(books)} книг -> {filename}')


def save_to_excel(books: list[dict], filename: str = EXCEL_FILE):
    if not books:
        logger.warning('Список книг пуст - CSV не создан')
        return

    df = pd.DataFrame(books)

    df = df.rename(columns={
        'title': "Название",
        'price': "Цена £",
        'rating': 'Рейтинг',

    })

    stats = df.groupby('Рейтинг').agg(
        Количество= ('Название', 'count'),
        Средняя_цена= ('Цена £', 'mean'),
        Мин_цена= ('Цена £', 'min'),
        Макс_цена= ('Цена £', 'max'),
    ).reset_index()


    for col in ['Средняя_цена', 'Мин_цена', 'Макс_цена']:
        stats[col] = stats[col].round(2)

    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Все книги', index=False)

        stats.to_excel(writer, sheet_name='По рейтингу', index=False)

    logger.info(f'EXCEL: сохранено {len(books)} книг -> {filename}')

