from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class BuyBody(Base):

    def __init__(self, driver, body_name_head):
        super().__init__(driver)
        self.driver = driver
        self.body_name_head = body_name_head
        # Добавляем переменные для сохранения значений
        self.saved_body_kod = None
        self.saved_body_price = None

    # Локаторы
    title = "//h1[@class='new-product__title']"
    body_kod = "//div[contains(@class, 'new-product-common-info__title') and contains(text(), 'Артикул:')]"
    body_price = "//div[contains(@class, 'new-product-params-price__value--current')]//span[@class='product-price-data']"
    button = "//button[contains(@class, 'button_for_product') and contains(@class, 'cart')]//span[contains(text(), 'В корзину')]"
    button_buy = "//a[contains(@class, 'button_for_top-cart-drop-down') and contains(text(), 'Оформить заказ')]"

    # Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_body_kod(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.body_kod)))

    def get_body_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.body_price)))

    def get_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button)))

    # Actions
    # Проверка заголовка
    def proverka_title_body(self):
        self.assert_word(self.get_title(), self.body_name_head)

    # Сохраняем код
    def save_body_kod(self):
        self.saved_body_kod = self.get_body_kod().text
        print(self.saved_body_kod)

    # Сохраняем цену
    def save_body_price(self):
        self.saved_body_price = self.get_body_price().text
        print(self.saved_body_price)

    # Клик в корзину
    def select_body_button_click(self):
        self.get_button().click()
        print('click get_button')

    # Клик оформить заказ
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('click checkout button')

    # Method
    def select_body_buy_cart(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/59686787')
        self.proverka_title_body()
        self.save_body_kod()
        self.save_body_price()
        self.select_body_button_click()
        self.click_checkout_button()

# python -m pytest -s -v