START_URL = 'https://books.toscrape.com/'

#Макс время ожидания появления элемента
TIMEOUT = 15

MAX_PAGES = 50

CSV_FILE = 'data/books_data.csv'
EXCEL_FILE = 'data/books_data.xlsx'

#True-запускается в фоне без вкладки, False - с открытием браузера
HEADLESS = False

RATING_MAP = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}