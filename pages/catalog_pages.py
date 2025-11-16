from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Catalog(Base):

    def __init__(self, driver, value_menu_catalog):
        super().__init__(driver)
        self.driver = driver
        self.value_menu_catalog = value_menu_catalog
        # Добавляем переменные для сохранения значений
        self.value_our_military = None
        self.value_figure_accessories = None

    # Локаторы
    title = "//div[normalize-space()='КАТАЛОГ']"
    catalog_our_military = "//a[text()='ОТЕЧЕСТВЕННЫЕ ВОЕННЫЕ']"
    catalog_figure_accessories = "//a[text()='АКСЕССУАРЫ ДЛЯ ФИГУРОК']"

    # Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_catalog_our_military(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_our_military)))

    def get_catalog_figure_accessories(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_figure_accessories)))

    # Actions
    # Проверка заголовока
    def proverka_title_catalog(self):
        self.assert_word(self.get_title(), self.value_menu_catalog)

    # Сохраняем названия разделов
    def name_our_military(self):
        self.value_our_military = self.get_catalog_our_military().text
        print(self.value_our_military)

    def name_figure_accessories(self):
        self.value_figure_accessories = self.get_catalog_figure_accessories().text
        print(self.value_figure_accessories)

    # Клик
    def click_catalog_our_military(self):
        self.get_catalog_our_military().click()
        print('click catalog_our_military')

    def click_catalog_figure_accessories(self):
        self.get_catalog_figure_accessories().click()
        print('click catalog_figure_accessories')

    # Metod
    def select_our_military(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products')
        self.proverka_title_catalog()
        self.name_our_military()
        self.get_catalog_our_military()
        self.click_catalog_our_military()

    def select_figure_accessories(self):
        self.get_current_url()
        self.assert_url('https://gsoldiers.ru/products')
        self.get_catalog_figure_accessories()
        self.name_figure_accessories()
        self.click_catalog_figure_accessories()


#  python -m pytest -s -v