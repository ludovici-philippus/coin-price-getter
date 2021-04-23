# Description: This program gets the price of cryptocurrencies in real time.
# Import the libs
from bs4 import BeautifulSoup
import requests
import time

class GetCryptoPrices():
    # Variables and constants
    CRYPTOS = ("bitcoin", "litecoin", "ethereum", "dolar", "euro")
    text = []
    #<div >
    #<span class="FCUp0c rQMQod">
    def get_crypto_price(self):
        # Make a request to the website
        for crypto in self.CRYPTOS:
            url = f"https://www.google.com/search?q={crypto}+hoje"
            HTML = requests.get(url)

            # Parse the HTML
            soup = BeautifulSoup(HTML.text, "html.parser")
            # Find the current price
            price = soup.find("div", attrs={"class" : "BNeawe iBp4i AP7Wnd"}).find("div", attrs={"class" : "BNeawe iBp4i AP7Wnd"}).text
            self.text.append(f"1 {crypto} = {price}")
        return self.text

get_crypto = GetCryptoPrices()
print(*get_crypto.get_crypto_price(), sep="; \n")
