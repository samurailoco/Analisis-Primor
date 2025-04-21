from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # sustituye al archivo
from selenium.webdriver.chrome.options import Options # opciones de chrome
from selenium.webdriver.common.by import By # By es para buscar por tag, clase, id...
from selenium.webdriver.support.ui import WebDriverWait   # para meter esperaras
from selenium.webdriver.support import expected_conditions as EC   # para esperar ciertos eventos
from selenium.webdriver import ActionChains # para hacer acciones con el ratón
import time
import random
import selenium.webdriver.common.keys as Keys # para simular teclas
import requests as req
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date
from bs4 import BeautifulSoup as bs
import pandas as pd

# Leer el archivo
df = pd.read_csv("/mnt/c/Users/danie/OneDrive/Desktop/Proyectos/Proyecto_PRIMOR/Data/raw.csv")

import ast

#convertir cadenas en listas
def parse_list(value):
    if isinstance(value, str):
        try:

            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return [value]
    else:
        return value

#columnas 'Vol(ml)' y 'Precio' sean listas
df['Vol(ml)'] = df['Vol(ml)'].apply(parse_list)
df['Precio'] = df['Precio'].apply(parse_list)

max_len = df[['Vol(ml)', 'Precio']].applymap(len).max(axis=1)  # Encuentra la longitud máxima por fila


df['Vol(ml)'] = df.apply(lambda row: row['Vol(ml)'] + [np.nan] * (max_len[row.name] - len(row['Vol(ml)'])), axis=1)
df['Precio'] = df.apply(lambda row: row['Precio'] + [np.nan] * (max_len[row.name] - len(row['Precio'])), axis=1)

# Desempaquetar ambas columnas con explode()
df_resultado = df.explode(['Vol(ml)', 'Precio'], ignore_index=True)

df=df_resultado
df.rename(columns={'Likes': 'Lista_deseos'}, inplace=True)
indicesM= [38,39,40,41,316,317,318,319,320,404,405,406,407,478,479,480,481,535,537,538,539,550,551,605,606,607,608,637,638,639,640,677,729,730,731,732,758,792,793,794,796,823,914,915,916,932,950,951,1057,1133,1164,1217,
1218,1219,1252,1262,1263,1264,1366,1367,1368,1369,1370,1506,1543,1555,1556,1557,1637,1657,1658,1659,1673,1674,1675,1759,1768,1788,1789,1815,1866,1867,1868,1916,1917,1918,1919,1924,1969,1992,2210,2331,
2335,2336,2337,2338,2339,2347,2352,2353,2374,2375,2376,2436,2448,2449,2450,2451,2453,2454,2464,2584,2585,2586,2587,2616,2622,2623,2637,2638,2642,2686,2687,2447,3054,3024,3699,3700,3701,3735,3736,3761,3778,3793,3794,
3799,3806,3808,3832,3833,3837,3838,3657,3658,3659,3660,3661,3655,3656,3541]

indicesH=[552, 553, 676, 966,1291,1292,1293,1427,1428,1429,1449,1450,1451,1641,1642,2047,2115,2116,2116,2163,2258,2259,2300,2117,2437,2438,2483,2508,2648,2669,3063,3064,3069,3712,3719,3720,3721,3764,3779,3780,3781,
3805,3819,3820,3830,3831,]

indicesUni=[554, 555, 556, 658, 659, 660,668, 669, 670, 671, 672, 695, 709, 710,778, 779, 780, 781,947,948,949, 975,988,989,1013,1062,1201,1202,1203,1204,1205,1206,1207,1297,1323,1324,1325,1488,1679,1732,
1760,1775,1870,1930,2039,2102,2011,2263,2268,2269,2270,2271,2111,2432,2530,2928,2929,3042,3710,3711,3754,3756,3757,3759,3760,3775,3802,3690,]

indicesNi=[1841,2010,2217,2225,2260,2431,2486,2541,3821,3822,]

df.loc[indicesM, 'Sexo']= 'Mujer'
df.loc[indicesH, 'Sexo']= 'Hombres'
df.loc[indicesUni, 'Sexo']= 'Unisex'
df.loc[indicesNi, 'Sexo']= 'Niños'

df.Sexo=df.Sexo.str.title().str.replace('Hombress','Hombres')
df.Concentracion=df.Concentracion.replace('EDP - Eau de Parfum','EDP').replace('EDT - Eau de Toilette','EDT').replace('EDC - Eau de Cologne','EDC')
df['Vol(ml)']=df['Vol(ml)'].replace('ml','').replace('EDT','').replace('EDP','').replace('EDC','').replace('ML','').replace('50 ml','50').replace('30 ml','30').replace('90 ml','90').replace('60 ml','60').replace('200 ml','200').replace('100 ml','100')
df['Vol(ml)']=df['Vol(ml)'].replace('40 ml','40').replace('25 ml','25').replace('75 ml','75').replace('35 ml','35').replace('80 ml','80').replace('125 ml','125').replace('150 ml','150')
df['Vol(ml)']=df['Vol(ml)'].replace('500 ml','500').replace('180 ml','180').replace('150 ml NO recargable','150').replace('15 ml NO recargable','15').replace('15 ml', '15')
df['Vol(ml)'].unique()
# Eliminar la palabra ' revisiones'
df['Reviews'] = df['Reviews'].str.replace(' revisiones', '', regex=False)

# Convertir la columna 'Reviews' a tipo numerico
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce').astype('Int64')
#sigo limpiando la columna Vol(ml)
indices150=[122,162,166,300,304,123,3153]
df.loc[indices150, 'Vol(ml)'] = 150

indices15 = [354, 359, 355, 360, 356, 361, 357, 362, 2487, 358, 363,3684, ]
df.loc[indices15, 'Vol(ml)'] = 15

indices20=[578,2314,2323]
df.loc[indices20, 'Vol(ml)'] = 20

indices250 = [465, 531, 466, 532, 467, 533, 468, 534]
df.loc[indices250, 'Vol(ml)'] = 250

indices100 = [3880, 3882, 3881, 3883, 29, 36, 14, 135, 425, 435, 445, 491, 501, 511, 743,1515,1525,1920]
df.loc[indices100, 'Vol(ml)'] = 100

indices50=[3673,3688,3674, 3689,3675, 3690]
df.loc[indices50, 'Vol(ml)'] = 50

indices200 = [3898, 3887, 3899, 3900]
df.loc[indices200, 'Vol(ml)'] = 200

df.loc[1596, 'Vol(ml)'] = 70

indicespre=[2630,3269,3287]
df.loc[indicespre, 'Precio'] = 5.5
df.replace('none', np.nan, inplace=True)
df.Sexo=df.Sexo.replace('Hombre','Hombres')
def convertir_likes(valor):
    if isinstance(valor, str) and 'K' in valor:
        return int(float(valor.replace('K', '')) * 1000)  # Elimina 'K' y multiplica por 1000
    else:
        return valor  
df.Fam_olfativa=df.Fam_olfativa.replace('Floral afrutada','Floral Frutal')

df['Lista_deseos'] = df['Lista_deseos'].apply(convertir_likes)
df['Lista_deseos'] = pd.to_numeric(df['Lista_deseos'], errors='coerce').fillna(0).astype(int)
df.Precio=df.Precio.str.replace(',','.').astype(float)
df['Rating/5'] = pd.to_numeric(df['Rating/5'], errors='coerce')

# Reemplazar <NA>, None, NaN y 0 
df = df.replace([pd.NA, np.nan, None, 0], pd.NA)
#creo una nueva columna con el valor por ml
df['Vol(ml)_num'] = pd.to_numeric(df['Vol(ml)'], errors='coerce')
df['Precio/ml'] = df['Precio'] / df['Vol(ml)_num'].round(2)
df['Rating/5'] = pd.to_numeric(df['Rating/5'], errors='coerce')
df['Precio/ml'] = pd.to_numeric(df['Precio/ml'], errors='coerce')

df.to_csv("/mnt/c/Users/danie/OneDrive/Desktop/Proyectos/Proyecto_PRIMOR/Data/processed.csv", index=False, encoding='utf-8')