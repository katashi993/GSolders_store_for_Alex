from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class FigureAccessories(Base):

    def __init__(self, driver, value_figure_accessories):
        super().__init__(driver)
        self.driver = driver
        self.value_figure_accessories = value_figure_accessories
        self.value_body_parts = None

    # Локаторы
    title = "//h1[@class='category-name']"
    body_parts = "//a[text()='Части тела']"
    # Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_body_parts(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.body_parts)))

    # Actions
    # Проверка заголовка
    def proverka_title_figure_accessories(self):
        self.assert_word(self.get_title(), self.value_figure_accessories)

    # Сохраняем названия разделов
    def name_body_parts(self):
        self.value_body_parts = self.get_body_parts().text
        print(self.value_body_parts)

    # Клик части тела
    def click_body_parts(self):
        self.get_body_parts().click()
        print('click body_parts')

    # Metod
    def select_body_parts(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products/category/aksessuari-1-6')
        self.proverka_title_figure_accessories()
        self.name_body_parts()
        self.click_body_parts()



#  python -m pytest -s -v