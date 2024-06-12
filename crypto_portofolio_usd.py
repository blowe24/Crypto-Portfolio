import pandas as pd
import requests
import matplotlib 
import matplotlib.pyplot as plt

# coingecko api for realtime crypto prices in usd
def get_price(crypto):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[crypto]['usd']

# wallets with out usdc
wallet1 = {
    'bitcoin': 0.00109253,
    'solana': 0.212818,
    'ethereum': 0.00413518
}

wallet2 = {
    'solana': 0.327454382,
}

# combine wallet amounts   
full_wallet = {}

for crypto, amount in wallet1.items():
    full_wallet[crypto] = full_wallet.get(crypto,0) + amount

for crypto, amount in wallet2.items():
    full_wallet[crypto] = full_wallet.get(crypto,0) + amount
    
# find usd value of full portfolio     
def calc_port(portfolio):
    total_value = 0
    for crypto, amount in portfolio.items():
        price = get_price(crypto)
        total_value += price * amount
    return total_value

print(calc_port(full_wallet))