from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class BodyParts(Base):

    def __init__(self, driver, value_body_parts):
        super().__init__(driver)
        self.driver = driver
        self.value_body_parts = value_body_parts
        # Добавляем переменные для сохранения значений
        self.value_men_head = None
        self.value_men_body = None

    # Локаторы
    title = "//h1[@class='category-name']"
    men_head = "//a[text()='Мужские головы']"
    men_body = "//a[text()='Мужские тела и части']"

    # Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_men_head(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.men_head)))

    def get_men_body(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.men_body)))

    # Actions
    # Проверка заголовока
    def proverka_title_body_parts(self):
        self.assert_word(self.get_title(), self.value_body_parts)

    # Сохраняем названия разделов
    def name_men_head(self):
        self.value_men_head = self.get_men_head().text
        print(self.value_men_head)

    def name_men_body(self):
        self.value_men_body = self.get_men_body().text
        print(self.value_men_body)

    # Клик
    def click_men_head(self):
        self.get_men_head().click()
        print('click men_head')

    def click_men_body(self):
        self.get_men_body().click()
        print('click men_body')

    # Metod
    def select_men_head(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/category/teloidi-1-6-body')
        self.proverka_title_body_parts()
        self.name_men_head()
        self.click_men_head()


    def select_men_body(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/category/teloidi-1-6-body')
        self.proverka_title_body_parts()
        self.name_men_body()
        self.click_men_body()

#  python -m pytest -s -v