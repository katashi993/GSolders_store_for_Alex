import datetime
from datetime import datetime, UTC
import re


class Base():
    def __init__(self, driver):
        self.driver = driver

    # получить текущий урл
    def get_current_url(self):
        get_url = self.driver.current_url
        print(get_url)
        return get_url

    # проверить текст элемента
    def assert_word(self, element_or_text, expected_text):
        actual_text = element_or_text.text if hasattr(element_or_text, 'text') else element_or_text
        assert actual_text == expected_text
        print('title - ok')

    # проверить что заголовок соответствует ожидаемому
    def assert_url(self, expected_url):
        assert self.driver.current_url == expected_url
        print('url - ok')

    # Извлечь последние 4 цифры из текста артикула
    def extract_last_4_digits(self, text):
        digits = re.findall(r'\d+', text)
        if digits:
            all_digits = ''.join(digits)
            return all_digits[-4:] if len(all_digits) >= 4 else all_digits
        return ""

    # Нормализовать цену - убрать пробелы и символы валюты
    def normalize_price(self, text):
        return text.replace(' ', '').replace('₽', '').strip()

    # Сравнить последние 4 цифры
    def assert_last_4_digits(self, element_or_text, expected_text):
        actual_text = element_or_text.text if hasattr(element_or_text, 'text') else element_or_text
        actual_digits = self.extract_last_4_digits(actual_text)
        expected_digits = self.extract_last_4_digits(expected_text)

        print(f"DEBUG: Ожидаемые последние 4 цифры: '{expected_digits}'")
        print(f"DEBUG: Фактические последние 4 цифры: '{actual_digits}'")
        assert actual_digits == expected_digits, f"Последние 4 цифры не совпадают! Ожидалось: {expected_digits}, Фактически: {actual_digits}"

    # Сравнить цены, игнорируя пробелы и символ валюты
    def assert_price(self, element_or_text, expected_text):
        actual_text = element_or_text.text if hasattr(element_or_text, 'text') else element_or_text
        actual_clean = self.normalize_price(actual_text)
        expected_clean = self.normalize_price(expected_text)

        print(f"DEBUG: Ожидаемая цена (очищенная): '{expected_clean}'")
        print(f"DEBUG: Фактическая цена (очищенная): '{actual_clean}'")
        assert actual_clean == expected_clean, f"Цены не совпадают! Ожидалось: {expected_clean}, Фактически: {actual_clean}"

    # Прокрутить к элементу
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # скрин
    def get_scr(self):
        date = datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
        screenshot_path = f'D:\\IT\\UI_stepik\\GSolders\\screen\\screen{date}.png'
        self.driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранен: {screenshot_path}")