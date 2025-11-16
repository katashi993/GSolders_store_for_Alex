from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class MenBody(Base):

    def __init__(self, driver, value_men_body):
        super().__init__(driver)
        self.driver = driver
        self.value_men_body = value_men_body
        # Добавляем переменные для сохранения значений
        self.men_body_name_value = None

    # Локаторы
    title = "//h1[@class='category-name']"
    men_head = "//a[contains(text(), 'Тело 1/6 (26060R-B)')]"

    # Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_men_head(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.men_head)))

    # Actions
    # Проверка заголовока
    def proverka_title_body_parts(self):
        self.assert_word(self.get_title(), self.value_men_body)

    # Сохраняем название тела
    def save_men_body_name(self):
        self.men_body_name_value = self.get_men_head().text
        print(self.save_men_body_name)

    # Клик
    def select_men_head_click(self):
        self.get_men_head().click()
        print('click men_head')

    # Metod
    def select_men_body_cart(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/category/mugskie-tela-teloidi-male-bodies-1-6')
        self.proverka_title_body_parts()
        self.save_men_body_name()
        self.select_men_head_click()

#  python -m pytest -s -v