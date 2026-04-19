import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchDriverException, TimeoutException)
from config import RATING_MAP

logger = logging.getLogger(__name__)


def parse_book_card(card) -> dict | None:
    try:
        title_element = card.find_element(By.CSS_SELECTOR, 'h3 a')
        title = title_element.get_attribute('title')

        #Цена
        price_text = card.find_element(By.CSS_SELECTOR, '.price_color').text
        price = float(price_text.replace('£', '').strip())

        #Rating

        rating_element = card.find_element(By.CSS_SELECTOR, 'p.star-rating')
        ratins_classes  = rating_element.get_attribute('class').split()
        rating_word = ratins_classes[-1] if len(ratins_classes) > 1 else 'One'
        rating = RATING_MAP.get(rating_word, 0)

        return {
            'title': title,
            'price': price,
            'rating': rating
        }

    except NoSuchDriverException as e:
        logger.warning(f'Ошибка обработки данных карточки {e}')
        return None
    except (ValueError, IndexError) as e:
        logger.warning(f'Ошибка обработки данных карточки {e}')
        return None


def parse_page(driver, wait: WebDriverWait) -> list[dict]:
    wait.until(EC.presence_of_all_elements_located((
        By.CSS_SELECTOR, 'article.product_pod'
    )))

    cards = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
    logger.info(f'Найдено карточек {len(cards)}')

    books = []

    for card in cards:
        book = parse_book_card(card)
        if book is not None:
            books.append(book)

    return books


def go_next_page(driver, wait: WebDriverWait) -> bool:
    try:
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.next a'))
        )

        url_before = driver.current_url
        next_button.click()

        wait.until(EC.url_changes(url_before))

        wait.until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR, 'article.product_pod'
            ))
        )
        return True

    except TimeoutException:
        return False

