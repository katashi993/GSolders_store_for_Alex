from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class BuySculpt(Base):

    def __init__(self, driver, sculpt_name_head):
        super().__init__(driver)
        self.driver = driver
        self.sculpt_name_head = sculpt_name_head
        # Добавляем переменные для сохранения значений
        self.saved_sculpt_kod = None
        self.saved_sculpt_price = None

    # Локаторы
    title = "//h1[@class='new-product__title']"
    sculpt_kod = "//div[contains(@class, 'new-product-common-info__title') and contains(text(), 'Артикул:')]"
    sculpt_price = "//div[contains(@class, 'new-product-params-price__value--current')]//span[@class='product-price-data']"
    button = "//button[contains(@class, 'button_for_product') and contains(@class, 'cart')]//span[contains(text(), 'В корзину')]"

    # Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_sculpt_kod(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.sculpt_kod)))

    def get_sculpt_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sculpt_price)))

    def get_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button)))

    # Actions
    # Проверка заголовока
    def proverka_title_men_head(self):
        self.assert_word(self.get_title(), self.sculpt_name_head)

    # Сохраняем код
    def save_men_head_kod(self):
        self.saved_sculpt_kod = self.get_sculpt_kod().text
        print(self.saved_sculpt_kod)

    # Сохраняем цену
    def save_sculpt_price(self):
        self.saved_sculpt_price = self.get_sculpt_price().text
        print(self.saved_sculpt_price)

    # Клик в корзину
    def select_men_head_button_click(self):
        self.get_button().click()
        print('click get_button')

    def go_back(self):
        self.driver.back()
        self.driver.back()
        print("back body parts")

    # Metod
    def select_men_head_buy_cart(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/59598660')
        self.proverka_title_men_head()
        self.save_men_head_kod()
        self.save_sculpt_price()
        self.select_men_head_button_click()
        self.go_back()

#  python -m pytest -s -v