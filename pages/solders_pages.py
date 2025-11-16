from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Solders(Base):

    def __init__(self, driver, value_price_solders, value_name_solders):
        super().__init__(driver)
        self.driver = driver
        self.value_price_solders = value_price_solders
        self.value_name_solders = value_name_solders
        # Добавляем переменные для сохранения значений
        self.value_kod_solders = None

    # Локаторы
    title = "//h1[@class='new-product__title']"
    img = "//img[@alt='Комплект снаряжения солдата 4-ой Сибирской стрелковой дивизии, Порт-Артур 1904  - Коллекционный НАБОР 1/6 scale Tsarist Russia East Siberia 4th Division in LuShunKou 1904 (QOM-1037) - QORANGE QOTOYS']"
    next = "//button[@id='new-product-overlay-btn--next']"
    close = "//button[@id='new-product-overlay-btn-close']"
    kod = "//div[@class='new-product-common-info__title']"
    cart_price = "//span[@class='product-price-data']"
    buy = "//button[.//span[text()='В корзину']]"

    # Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_img(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.img)))

    def get_next(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.next)))

    def get_close(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.close)))

    def get_kod(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.kod)))

    def get_cart_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_price)))

    def get_buy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.buy)))

    # Actions
    # Проверка заголовка
    def proverka_name_solders(self):
        self.assert_word(self.get_title(), self.value_name_solders)

    # Проверка цены солдатика
    def proverka_price_solders(self):
        self.value_cart_price_solders = self.get_cart_price().text
        expected_price = self.value_price_solders.replace(' ₽', '')
        self.assert_word(self.value_cart_price_solders, expected_price)

    # Просмотр фото
    def click_img(self):
        self.get_img().click()
        print('click image')

    def click_next(self):
        for _ in range(10):
            self.get_next().click()
        print('click photo solders')

    def click_close_photo(self):
        self.get_close().click()
        print('click close photo')

    # Сохраняем код солдатика
    def save_kod_solders(self):
        self.value_kod_solders = self.get_kod().text
        print(self.value_kod_solders)


    # Добавить солдатика в корзину
    def click_buy_solders(self):
        self.get_buy().click()
        print('click buy_solders')

    # Возврат в каталог
    def go_back(self):
        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.driver.back()
        print("back catalog")

    # Metod
    def select_solders_cart(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/qom-1037')
        self.proverka_name_solders()
        self.proverka_price_solders()
        self.click_img()
        self.click_next()
        self.click_close_photo()
        self.save_kod_solders()
        self.click_buy_solders()
        self.go_back()


#  python -m pytest -s -v