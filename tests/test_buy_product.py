from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_pages import MainPages
from pages.catalog_pages import Catalog
from pages.our_military_pages import OurMilitary
from pages.solders_pages import Solders
from pages.figure_accessories_pages import FigureAccessories
from pages.body_parts_pages import BodyParts
from pages.men_head_pages import MenHead
from pages.buy_men_sculpt_pages import BuySculpt
from pages.men_body_pages import MenBody
from pages.buy_men_body_pages import BuyBody
from pages.cart_buy_pages import CartBuy
import time

def test_buy_product():
    service = Service('D:\\IT\\UI_stepik\\GSolders\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=service, options=options)

    print('Start test')

    mp = MainPages(driver)
    mp.select_menu_catalog()

    catalog = Catalog(driver, mp.value_menu_catalog)
    catalog.select_our_military()

    om = OurMilitary(driver, catalog.value_our_military)
    om.select_our_military()

    solders = Solders(driver, om.value_price_solders, om.value_name_solders)
    solders.select_solders_cart()

    catalog = Catalog(driver, mp.value_menu_catalog)
    catalog.select_figure_accessories()

    fa = FigureAccessories(driver, catalog.value_figure_accessories)
    fa.select_body_parts()

    bp = BodyParts(driver, fa.value_body_parts)
    bp.select_men_head()

    mh = MenHead(driver, bp.value_men_head)
    mh.select_men_head()

    bms = BuySculpt(driver, mh.sculpt_name_head)
    bms.select_men_head_buy_cart()

    bp = BodyParts(driver, fa.value_body_parts)
    bp.select_men_body()

    mb = MenBody(driver, bp.value_men_body)
    mb.select_men_body_cart()

    bmb = BuyBody(driver, mb.men_body_name_value)
    bmb.select_body_buy_cart()

    cp = CartBuy(driver, solders.value_kod_solders, om.value_name_solders, om.value_price_solders, bms.saved_sculpt_kod,
                 bms.saved_sculpt_price, mh.sculpt_name_head, mb.men_body_name_value, bmb.saved_body_kod,
                 bmb.saved_body_price)
    cp.check_all_cart_items()

    print('End test')
    time.sleep(5)