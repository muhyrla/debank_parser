import requests

url = "https://debank-unofficial-wallet-portfolio-balance-api.p.rapidapi.com/user/total_balance"

querystring = {"address":"0x58962c722A7be0841C9489c1026e01E4f52EA2C7"}

headers = {
	"X-RapidAPI-Key": "ea510787b3mshaa41343b55a2f89p178ce5jsn306a286ac1eb",
	"X-RapidAPI-Host": "debank-unofficial-wallet-portfolio-balance-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json()['total_usd_value'])