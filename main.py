import time
import requests


def get_balance(address):
    url = "https://debank-unofficial-wallet-portfolio-balance-api.p.rapidapi.com/user/total_balance"

    querystring = {"address":address}

    headers = {
        "X-RapidAPI-Key": "ea510787b3mshaa41343b55a2f89p178ce5jsn306a286ac1eb",
        "X-RapidAPI-Host": "debank-unofficial-wallet-portfolio-balance-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return float(response.json()['total_usd_value'])


if __name__ == "__main__":
    with open('wallets.txt', 'r') as f:
        wallets = f.readlines()
        all_networth = 0.0
        for wallet in wallets:
            wallet = wallets[0].replace('\n', '')
            networth = get_balance(wallet)
            print(f'{wallet} networth: {networth}')
            all_networth+=networth
        
        print(f"Accounts networth: {all_networth}")