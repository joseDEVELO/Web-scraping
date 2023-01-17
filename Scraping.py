import requests
from bs4 import BeautifulSoup

#colores
azul = "\33[1;36m"
blanco = "\33[1;37m"  



# Llamando a la url de la web
url = "https://www.tiendagamermedellin.co/pc-ryzen-5-5600g-rx-vega"
nombreTienda = url.split("/")[2]
# Personalizando headers
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"}
# Obteniendo respuestas
res = requests.get(url, headers=headers)
res.status_code # Estado de la respuesta
# Implementando BeautifullSoup
sopa = BeautifulSoup(res.text, "html.parser")

# Llamando al titulo
#sopa.title
#<title>PC / RYZEN 5 5600G + RX VEGA | Tienda Gamer Medellin</title>
titulo = sopa.title.text
#'PC / RYZEN 5 5600G + RX VEGA | Tienda Gamer Medellin'

# sopa.find("h1", class_="product-heading__title")
#<h1 class="product-heading__title">PC / RYZEN 5 5600G + RX VEGA</h1>
tituloH1 = sopa.find("h1", class_="product-heading__title").text
#'PC / RYZEN 5 5600G + RX VEGA'

# Llamando al elemento de precios
#sopa.find("h2", class_="product-heading__pricing product-heading__pricing--has-discount")
# <h2 class="product-heading__pricing product-heading__pricing--has-discount">
# <span>$3.192.000 COP</span>
# <span>$3.360.000 COP</span>
# </h2>
precioRebajado = sopa.find("h2", class_="product-heading__pricing product-heading__pricing--has-discount").find_all("span")
precioAnterior = sopa.find("h2", class_="product-heading__pricing product-heading__pricing--has-discount").find_all("span")[1]

# Obteniendo la imagen del producto 
imagen = sopa.find(class_="product-gallery__image").attrs.get("src")
#'https://cdnx.jumpseller.com/tienda-gamer-medellin/image/30647310/resize/610/610?1672721839'

print("Obteniendo datos de la web: ", nombreTienda)
print()
print(f"{azul}url obtenida:  {blanco} {url}")
print(f"{azul}titulo de la web: {blanco} {titulo}")
print(f"{azul}titulo del articulo:  {blanco} {tituloH1}")
print(f"{azul}imagen del articulo {blanco} {imagen}")
print(f"{azul}Precio actual  {blanco} {precioRebajado}")
print(f"{azul}Precio anterior: , {blanco} {precioAnterior}")