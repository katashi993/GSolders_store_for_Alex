from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class MainPages(Base):

    url = 'https://gsoldiers.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Добавляем переменные для сохранения значений
        self.value_menu_catalog = None

    # Локаторы
    menu_catalog = "//a[text()='КАТАЛОГ']"

    # Getters
    def get_menu_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_catalog)))

    # Actions
    # сохраняем названия разделов
    def name_menu_catalog(self):
        self.value_menu_catalog = self.get_menu_catalog().text
        print(self.value_menu_catalog)

    # Клик по разделу
    def click_menu_catalog(self):
        self.get_menu_catalog().click()
        print('click menu_catalog')

    # Metod
    def select_menu_catalog(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.get_menu_catalog()
        self.name_menu_catalog()
        self.click_menu_catalog()

#  python -m pytest -s -v