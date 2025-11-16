from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class MenHead(Base):

    def __init__(self, driver, value_men_head):
        super().__init__(driver)
        self.driver = driver
        self.value_men_head = value_men_head
        # Добавляем переменные для сохранения значений
        self.sculpt_name_head = None

    # Локаторы
    title = "//h1[@class='category-name']"
    men_head = "//a[text()='Скульпт 1/6 (78095) - DAMTOYS']"

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
        self.assert_word(self.get_title(), self.value_men_head)

    # Сохраняем название скульпта
    def save_men_head(self):
        self.sculpt_name_head = self.get_men_head().text
        print(self.sculpt_name_head)

    # Клик
    def select_men_head_click(self):
        self.get_men_head().click()
        print('click select_men_head')

    # Metod
    def select_men_head(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/category/mugskie-golovi-skulpti-male-heads-1-6')
        self.proverka_title_body_parts()
        self.save_men_head()
        self.select_men_head_click()

#  python -m pytest -s -v