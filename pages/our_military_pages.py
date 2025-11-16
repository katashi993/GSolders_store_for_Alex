from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base

class OurMilitary(Base):

    def __init__(self, driver, value_our_military):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)
        self.value_our_military = value_our_military
        # Добавляем переменные для сохранения значений
        self.value_price_solders = None
        self.value_name_solders = None

    # Локаторы
    title = "//div[normalize-space()='ОТЕЧЕСТВЕННЫЕ ВОЕННЫЕ']"
    cb = "//div[normalize-space()='В наличии']"
    price_min = "//input[@id='catalog_price_filter_min_cost']"
    price_max = "//input[@id='catalog_price_filter_max_cost']"
    solders = "//a[contains(text(), 'Комплект снаряжения солдата 4-ой Сибирской стрелковой дивизии')]"
    price_solders = "//div[@class='product-item-price']"

    # Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cb)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_solders(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.solders)))

    def get_price_solders(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_solders)))

    # Actions
    # Проверка заголовка
    def proverka_title_our_military(self):
        self.assert_word(self.get_title(), self.value_our_military)

    # Фильтр
    def click_checkbox(self):
        self.get_checkbox().click()
        print('click checkbox')

    def new_value_price_min(self):
        self.get_price_min().click()
        self.action.double_click(self.get_price_min()).perform()
        self.get_price_min().send_keys(Keys.BACKSPACE *10)
        self.get_price_min().send_keys('17000')
        print('new value min price 17000')

    def new_value_price_max(self):
        self.get_price_max().click()
        self.action.double_click(self.get_price_max()).perform()
        self.get_price_max().send_keys(Keys.BACKSPACE *10)
        self.get_price_max().send_keys('20000')
        self.get_price_max().send_keys(Keys. RETURN)
        print('new value max price 20000')

    # Сохраняем цену солдатика
    def save_price_solders(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.price_solders))
        )
        self.value_price_solders = self.get_price_solders().text
        print(self.value_price_solders)

    # Сохраняем название солдатика
    def save_name_our_military(self):
        self.value_name_solders = self.get_solders().text
        print(self.value_name_solders)

    # Просмотр страницы солдатика
    def click_solders_page(self):
        self.get_solders().click()
        print('click get_solders')

    # Metod
    def select_our_military(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/category/damtoys')
        self.proverka_title_our_military()
        self.click_checkbox()
        self.new_value_price_min()
        self.new_value_price_max()
        self.save_price_solders()
        self.save_name_our_military()
        self.click_solders_page()


#  python -m pytest -s -v