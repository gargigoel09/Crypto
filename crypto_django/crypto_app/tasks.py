# tasks.py

from celery import shared_task
import requests
from .models import Coin


@shared_task
def update_coin_prices():
    coins = Coin.objects.all()  # Retrieve coins from the database
    for coin in coins:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin.symbol}&vs_currencies=usd")
        if response.status_code == 200:
            coin_data = response.json()
            coin_price = coin_data.get(coin.symbol, {}).get("usd")
            if coin_price is not None:
                coin.price = coin_price
                coin.save()
