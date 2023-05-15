from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# url
url = 'https://www.latamairlines.com/co/es/ofertas-vuelos?origin=BGA&inbound=2023-05-20T17%3A00%3A00.000Z&outbound=2023-05-19T17%3A00%3A00.000Z&destination=BOG&adt=1&chd=0&inf=0&trip=RT&cabin=Economy&redemption=false&sort=RECOMMENDED'
# Ruta del archivo chromedrive
chromedriver_path = '---/chromedriver'

# Crear un objeto service
service = Service(chromedriver_path)

# Crear el controlador de chrome
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(service=service, options=options)

# Abrir una pagina web
driver.get(url)

# Esperar unos segundos
driver.implicitly_wait(5)

vuelos = driver.find_elements('xpath', '//ol/li')
print('vuelos', vuelos)

# seleccionamos el primer vuelo
vuelo_1 = vuelos[1]
print('vuelo_1', vuelo_1)

# hora de salida
hora_de_salida = vuelo_1.find_element(
    'xpath', '//div[@class="card-flightstyle__ContainerFlightInfo-sc__sc-16r5pdw-15 cPzcrG flight-information"]/span[1]').text
print('hora de salida', hora_de_salida)

# link escalas
link_escalas = vuelo_1.find_element(
    'xpath', '//div[@class ="card-flightstyle__ContainerFooterCard-sc__sc-16r5pdw-24 iMBDQD"]/a')
print('escalas', link_escalas)
link_escalas.click()

# Paradas
paradas = link_escalas.find_element(
    'xpath', '//section[@class="itinerarystyle__Section-sc__sc-1n97ky6-1 ddwMQK"]')
print('paradas', paradas)

try:
    escalas = len(paradas)-1
    print('escalas', escalas)
except Exception as e:
    escalas = 0
    print('escalas', escalas)
# Esperar a que el usuario presione una tecla para cerrar el navegador
input("Presionar una tela para cerrar el navegador")

driver.quit()
