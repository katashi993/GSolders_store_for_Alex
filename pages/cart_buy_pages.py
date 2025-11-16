from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartBuy(Base):
    def __init__(self, driver, value_kod_solders, value_name_solders, value_price_solders, saved_sculpt_kod,
                 saved_sculpt_price, sculpt_name_head, body_name_head, saved_body_kod, saved_body_price):
        super().__init__(driver)
        self.driver = driver

        self.value_kod_solders = value_kod_solders
        self.value_name_solders = value_name_solders
        self.value_price_solders = value_price_solders

        self.saved_sculpt_kod = saved_sculpt_kod
        self.saved_sculpt_price = saved_sculpt_price
        self.sculpt_name_head = sculpt_name_head

        self.body_name_head = body_name_head
        self.saved_body_kod = saved_body_kod
        self.saved_body_price = saved_body_price

    # Локаторы
    cart_page_title = "//h1[contains(text(), 'Корзина')]"
    cart_progress_step = "//div[contains(@class, 'cart-step') and contains(@class, 'active')]"

    komplekt_snaryageniya_name = "(//div[@id='item58469080']//a[@class='blue -break'])[1]"
    komplekt_snaryageniya_kod = "(//div[@id='item58469080']//div[@class='scu'])[1]"
    komplekt_snaryageniya_price = "(//div[@id='item58469080']//span[@class='price-info product-summ'])[1]"

    skulpt_name = "(//div[@id='item59598660']//a[@class='blue -break'])[1]"
    skulpt_kod = "(//div[@id='item59598660']//div[@class='scu'])[1]"
    skulpt_price = "(//div[@id='item59598660']//span[@class='price-info product-summ'])[1]"

    telo_name = "(//div[@id='item59686787']//a[@class='blue -break'])[1]"
    telo_kod = "(//div[@id='item59686787']//div[@class='scu'])[1]"
    telo_price = "(//div[@id='item59686787']//span[@class='price-info product-summ'])[1]"

    total_price = "//span[@class='js-cart__total']"
    total_summ_block = "//p[@class='price' and @id='total-summ']"

    # Getters
    def get_cart_page_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_page_title)))

    def get_cart_progress_step(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_progress_step)))

    def get_komplekt_snaryageniya_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.komplekt_snaryageniya_name)))

    def get_komplekt_snaryageniya_kod(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.komplekt_snaryageniya_kod)))

    def get_komplekt_snaryageniya_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.komplekt_snaryageniya_price)))

    def get_skulpt_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.skulpt_name)))

    def get_skulpt_kod(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.skulpt_kod)))

    def get_skulpt_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.skulpt_price)))

    def get_telo_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.telo_name)))

    def get_telo_kod(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.telo_kod)))

    def get_telo_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.telo_price)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.total_price)))

    def get_total_summ_block(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.total_summ_block)))

    # Actions
    def check_cart_page(self):
        """Проверка что мы находимся на странице корзины"""
        # Проверяем URL
        expected_url = "https://gsoldiers.ru/products/viewcart"
        self.assert_url(expected_url)

        # Проверяем заголовок страницы "Корзина"
        cart_title = self.get_cart_page_title()
        self.assert_word(cart_title, "Корзина")
        print("Заголовок страницы 'Корзина' - OK")

        # Проверяем что активен первый шаг "Товары"
        cart_progress = self.get_cart_progress_step()
        progress_text = cart_progress.text
        assert "Товары" in progress_text or "1" in progress_text, f"Активный шаг не 'Товары': {progress_text}"
        print("Активный шаг 'Товары' - OK")

        print("Проверка страницы корзины завершена успешно")

    def check_komplekt_snaryageniya(self):
        # Проверка названия снаряжения
        komplekt_name = self.get_komplekt_snaryageniya_name()
        print(f"DEBUG Название в корзине: {komplekt_name.text}")
        print(f"DEBUG Ожидаемое название: {self.value_name_solders}")
        self.assert_word(komplekt_name, self.value_name_solders)

        # Проверка кода снаряжения (только последние 4 цифры)
        komplekt_kod = self.get_komplekt_snaryageniya_kod()
        print(f"DEBUG Код в корзине: {komplekt_kod.text}")
        print(f"DEBUG Ожидаемый код: {self.value_kod_solders}")
        self.assert_last_4_digits(komplekt_kod, self.value_kod_solders)

        # Проверка цены снаряжения
        komplekt_price = self.get_komplekt_snaryageniya_price()
        print(f"DEBUG Цена в корзине: {komplekt_price.text}")
        print(f"DEBUG Ожидаемая цена: {self.value_price_solders}")
        self.assert_price(komplekt_price, self.value_price_solders)

    def check_skulpt(self):
        # Проверка названия скульптуры
        skulpt_name = self.get_skulpt_name()
        print(f"DEBUG Скульптура в корзине: {skulpt_name.text}")
        print(f"DEBUG Ожидаемая скульптура: {self.sculpt_name_head}")
        self.assert_word(skulpt_name, self.sculpt_name_head)

        # Проверка кода скульптуры (только последние 4 цифры)
        skulpt_kod = self.get_skulpt_kod()
        print(f"DEBUG Код скульптуры в корзине: {skulpt_kod.text}")
        print(f"DEBUG Ожидаемый код скульптуры: {self.saved_sculpt_kod}")
        self.assert_last_4_digits(skulpt_kod, self.saved_sculpt_kod)

        # Проверка цены скульптуры
        skulpt_price = self.get_skulpt_price()
        print(f"DEBUG Цена скульптуры в корзине: {skulpt_price.text}")
        print(f"DEBUG Ожидаемая цена скульптуры: {self.saved_sculpt_price}")
        self.assert_price(skulpt_price, self.saved_sculpt_price)

    def check_telo(self):
        # Проверка названия тела
        telo_name = self.get_telo_name()
        print(f"DEBUG Тело в корзине: {telo_name.text}")
        print(f"DEBUG Ожидаемое тело: {self.body_name_head}")
        self.assert_word(telo_name, self.body_name_head)

        # Проверка кода тела (только последние 4 цифры)
        telo_kod = self.get_telo_kod()
        print(f"DEBUG Код тела в корзине: {telo_kod.text}")
        print(f"DEBUG Ожидаемый код тела: {self.saved_body_kod}")
        self.assert_last_4_digits(telo_kod, self.saved_body_kod)

        # Проверка цены тела
        telo_price = self.get_telo_price()
        print(f"DEBUG Цена тела в корзине: {telo_price.text}")
        print(f"DEBUG Ожидаемая цена тела: {self.saved_body_price}")
        self.assert_price(telo_price, self.saved_body_price)

    def check_total_price(self):
        # Получаем цены товаров и преобразуем в числа
        komplekt_price_text = self.get_komplekt_snaryageniya_price().text
        skulpt_price_text = self.get_skulpt_price().text
        telo_price_text = self.get_telo_price().text

        print(f"DEBUG Цена комплекта: {komplekt_price_text}")
        print(f"DEBUG Цена скульптуры: {skulpt_price_text}")
        print(f"DEBUG Цена тела: {telo_price_text}")

        # Преобразуем цены в числа
        komplekt_price_value = float(self.normalize_price(komplekt_price_text))
        skulpt_price_value = float(self.normalize_price(skulpt_price_text))
        telo_price_value = float(self.normalize_price(telo_price_text))

        # Считаем ожидаемую общую цену
        expected_total = komplekt_price_value + skulpt_price_value + telo_price_value

        # Получаем фактическую общую цену
        total_price_element = self.get_total_price()

        # Прокручиваем к блоку с итоговой ценой
        total_summ_block = self.get_total_summ_block()
        self.scroll_to_element(total_summ_block)
        print("Прокрутили к блоку с итоговой ценой 'Итого: 25500 ₽'")

        total_price_text = total_price_element.text
        actual_total = float(self.normalize_price(total_price_text))

        print(f"DEBUG Ожидаемая общая цена: {expected_total}")
        print(f"DEBUG Фактическая общая цена: {actual_total}")

        # Проверяем соответствие
        assert expected_total == actual_total, \
            f"Общая цена не совпадает! Ожидалось: {expected_total}, Фактически: {actual_total}"

        print(f"Проверка общей цены успешна: {actual_total}")

        # Делаем скриншот с итоговой ценой
        self.get_scr()
        print("Скриншот с итоговой ценой сохранен")

    def check_all_cart_items(self):
        # Сначала проверяем что мы на правильной странице
        self.check_cart_page()

        # Затем проверяем все товары в корзине
        self.check_komplekt_snaryageniya()
        self.check_skulpt()
        self.check_telo()
        self.check_total_price()
        print("Все 11 проверок пройдены: 1 страница корзины, 3 названия, 3 кода, 3 цены, 1 общая цена - OK")

#  python -m pytest -s -v