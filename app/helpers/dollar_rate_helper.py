import requests
from PyQt5.QtWidgets import QDoubleSpinBox

from bs4 import BeautifulSoup as Soup


def get_average_sell_dollar_rate() -> float:
    url: str = 'https://minfin.com.ua/ua/currency/auction/'
    page = requests.get(url)
    page_soup = Soup(page.content, 'html.parser')
    html_prices = page_soup.findAll(name='span', attrs={"class": "Typography cardHeadlineL align"})
    sell_price: str = html_prices[1].next
    return float(sell_price.replace(',', '.', 1))
