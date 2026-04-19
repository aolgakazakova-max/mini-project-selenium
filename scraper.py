import logging
import statistics
from collections import Counter
from selenium.webdriver.support.ui import WebDriverWait

from config import START_URL, TIMEOUT, MAX_PAGES
from driver_setup import create_driver
from parser import parse_page, go_next_page
from saver import save_to_csv, save_to_excel

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def collect_books() -> list[dict]:
    driver = create_driver()
    wait = WebDriverWait(driver, timeout=TIMEOUT)

    all_books = []
    page_num = 1


    driver.get(START_URL)
    logger.info(f'Открыт сайт {START_URL}')
    logger.info('-'*50)

    while page_num <= MAX_PAGES:
        logger.info(f'Страница {page_num} | {driver.current_url}')

        book_on_page = parse_page(driver, wait)
        logger.info(f'Данные собраны {book_on_page}')
        all_books.extend(book_on_page)

        logger.info(
            f'Получили {len(book_on_page)}'
            f'Всего {len(all_books)}'
        )

        if not go_next_page(driver, wait):
            logger.info('-'*50)
            logger.info(f'Последняя страница достигнута {page_num}')
            break

        page_num += 1
    return all_books




def main():
    books = collect_books()

    if not books:
        logger.error('Данные не собраны. Проверьте ошибки выше')
        return

    save_to_csv(books)
    save_to_excel(books)


if __name__ == '__main__':
    main()