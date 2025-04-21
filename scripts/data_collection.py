from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from datetime import datetime
from datetime import date
import time
import random
import selenium.webdriver.common.keys as Keys
import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bs

pd.options.display.max_columns = 22

# Configuración de las opciones de Chrome
opciones = webdriver.ChromeOptions()
opciones.add_argument('window-size=1000,1400')
opciones.add_argument('--disable-extensions')
opciones.add_argument('--disable-blink-features=AutomationControlled')
opciones.add_argument('--no-sandbox')
opciones.add_experimental_option('useAutomationExtension', False)
opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_argument('--incognito')  # Modo incognito

# Abriendo el navegador
url = 'https://www.primor.eu/es_es/perfumes'
driver = webdriver.Chrome(options=opciones)
driver.get(url)

# Rechazando cookies
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="am-cookie-bar"]/div/div/div/div/div/button[2]'))).click()

# Función para extraer características del perfume
def perfumes_caracteristicas():
    time.sleep(2)
    soup = bs(driver.page_source, 'html.parser')

    try:
        marca = soup.find('a', {'class': 'font-bold uppercase'}).text.split('\n')[1].strip()
        nombre = soup.find('span', {'class': 'base text-[.9em] md:text-[1em]'}).text.split('-')[0]
        tipo = soup.find('h2', {'class': 'text-sm md:text-lg'}).text
        sexo = tipo.split(' ')[-1]
    except:
        marca, nombre, tipo, sexo = 'none', 'None', 'none', 'none'

    try:
        precio = soup.find('span', {'class': 'price'}).text.split("\xa0")[0]
    except:
        precio = 'none'

    try:
        volumen = driver.find_element(By.XPATH, '//*[@id="product_addtocart_form"]/div/div/div/div/div/div/div[1]/label/div/div[1]').text
    except:
        volumen = 'none'

    try:
        ratings = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[1]/section/div[2]/div[3]')
        rating = ratings.find_elements(By.TAG_NAME, 'p')[0].text.split('-')[0]
        review = ratings.find_elements(By.TAG_NAME, 'p')[0].text.split('-')[1]
    except:
        rating, review = 'none', 'none'

    try:
        likes = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[1]/section/div[2]/div[4]').text.split('\n')[2]
    except:
        likes = 'none'

    try:
        concentracion = soup.find('tr', {'id': 'product-attribute-concentracion'}).text.split('\n')[4].strip()
    except:
        concentracion = 'none'

    try:
        famolf = soup.find('tr', {'id': 'product-attribute-familia_olfativa'}).text.split('\n')[4].strip()
    except:
        famolf = 'none'

    try:
        formato = soup.find('tr', {'id': 'product-attribute-formato'}).text.split('\n')[4].strip()
    except:
        formato = 'none'

    try:
        corazon = soup.find('tr', {'id': 'product-attribute-notas_corazon'}).text.split('\n')[4].strip()
    except:
        corazon = 'none'

    try:
        fondo = soup.find('tr', {'id': 'product-attribute-notas_fondo'}).text.split('\n')[4].strip()
    except:
        fondo = 'none'

    try:
        salida = soup.find('tr', {'id': 'product-attribute-notas_salida'}).text.split('\n')[4].strip()
    except:
        salida = 'none'

    return {
        'Nombre': nombre,
        'Marca': marca,
        'Tipo': tipo,
        'Sexo': sexo,
        'Rating/5': rating,
        'Reviews': review,
        'Vol(ml)': volumen,
        'Precio': precio,
        'Lista_deseos': likes,
        'Concentracion': concentracion,
        'Formato': formato,
        'Fam_olfativa': famolf,
        'Notas_Corazon': corazon,
        'Notas_Fondo': fondo,
        'Notas_salida': salida
    }

# Función para navegar por las páginas de perfumes
def navegar_por_paginas():
    DFfinal = []
    while True:
        # Extraer productos de la página actual
        productos_elementos = [f'//*[@id="product-list"]/div[2]/ul/li[{i}]/form' for i in range(1, 49)]
        for ruta in productos_elementos:
            try:
                button = driver.find_element(By.XPATH, ruta)
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                time.sleep(1)
                button.click()
                datos = perfumes_caracteristicas()
                DFfinal.append(datos)
                time.sleep(1.5)
            except Exception as e:
                print(f'Error con producto: {e}')

        # Intentar avanzar a la siguiente página
        try:
            boton_siguiente = driver.find_element(By.XPATH, '//*[@id="product-list"]/div[3]/div/div/nav/ol/li[6]')
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton_siguiente)
            boton_siguiente.click()
            WebDriverWait(driver, 10).until(EC.staleness_of(boton_siguiente))  # Esperar a que cargue la siguiente página
            time.sleep(3)
        except:
            print("No hay más páginas.")
            break

    return DFfinal

# Iniciar la navegación
navegar_por_paginas()

# Cerrar el navegador
driver.quit()
