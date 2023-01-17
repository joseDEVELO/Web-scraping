import requests
from bs4 import BeautifulSoup


url = "https://www.tiendagamermedellin.co/pc-ryzen-5-5600g-rx-vega"

headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"}

res = requests.get(url, headers=headers)
res.status_code

