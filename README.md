# 🧴 Análisis de productos de perfumería PRIMOR

Este proyecto consiste en el **scrapeo, limpieza, análisis y visualización** de más de **4000 productos de perfumería** obtenidos del sitio web [Primor](https://www.primor.eu/). El objetivo es realizar un análisis profundo del mercado digital de perfumería en España, identificando patrones, tendencias y características clave de los productos, marcas y sus atributos aromáticos.

---

## 🛠️ Tecnologías utilizadas

- 🐍 **Python 3.10+**
- 🧪 **BeautifulSoup** y **Selenium** para el web scraping  
- ⏱️ `time`, `random`, `re` para control de scroll y limpieza básica
- 📊 **pandas**, **numpy** para manipulación de datos
- 📈 **seaborn**, **matplotlib**, **plotly** para visualización
- 🧼 Técnicas de limpieza y tratamiento de texto para datos no estructurados

---

## 🔍 Objetivos del proyecto

- Automatizar la recolección de datos de productos en la tienda online PRIMOR.
- Construir una base de datos estructurada con información detallada de cada producto.
- Identificar y analizar patrones en:
  - **Marcas más relevantes**
  - **Precios por tipo y formato**
  - **Distribución por sexo y concentración**
  - **Familias olfativas más comunes**
  - **Notas de salida, corazón y fondo**
- Visualizar métricas clave para comunicar hallazgos de forma clara y efectiva.

---

## 📦 Estructura del dataset

| Columna           | Descripción                                             |
|-------------------|---------------------------------------------------------|
| `Nombre`          | Nombre del producto                                     |
| `Marca`           | Marca o fabricante                                      |
| `Tipo`            | Tipo de producto (eau de parfum, colonia, etc.)         |
| `Sexo`            | Público objetivo (Hombre, Mujer, Unisex)               |
| `Rating/5`        | Puntuación promedio de los usuarios                     |
| `Reviews`         | Número de reseñas                                        |
| `Vol(ml)`         | Volumen en mililitros                                   |
| `Precio`          | Precio del producto                                     |
| `Lista_deseos`    | Número de usuarios que añadieron el producto a favoritos |
| `Concentracion`   | Nivel de concentración (Parfum, Eau de Toilette, etc.)  |
| `Formato`         | Formato del producto (spray, miniatura, etc.)           |
| `Fam_olfativa`    | Familia olfativa principal                              |
| `Notas_salida`    | Notas aromáticas de salida                              |
| `Notas_Corazon`   | Notas aromáticas de corazón                             |
| `Notas_Fondo`     | Notas aromáticas de fondo                               |

---

## 📊 Análisis realizados

- Distribución de precios por volumen y concentración
- Marcas con mayor variedad y presencia en el catálogo
- Formatos más comunes por tipo de producto
- Distribución de productos por sexo y familia olfativa
- Frecuencia y coocurrencia de notas aromáticas
- Comparativa entre las fragancias más deseadas y mejor valoradas
- Gráficos de densidad para identificar rangos de precios frecuentes
- Nubes de palabras con las notas aromáticas más comunes

---

## 📉 Visualizaciones destacadas

- Histogramas de precios y volúmenes
- Mapas de calor para la relación entre marcas y familias olfativas
- Gráficos de dispersión para comparar precio vs. volumen
- Barras agrupadas para distribución por sexo y formato
- Wordclouds de notas de salida, corazón y fondo

---

## ⚠️ Limitaciones

- Algunos productos presentan errores ortográficos, fichas incompletas o precios atípicos, que fueron corregidos o tratados durante la limpieza.
- El sitio web no ofrece una API, por lo que el scraping depende de la estructura HTML y puede romperse si el sitio cambia.
- Por **protección de datos sensibles de la empresa**, se omiten ciertos análisis detallados que podrían revelar información estratégica.

---

## 📁 Estructura del proyecto
📂 proyecto-primor-perfumeria/

├── data/
│   ├── raw_data.csv
│   └── processed_data.csv

├── notebooks/
│   ├── scraping.ipynb
│   ├── limpieza_y_transformacion.ipynb
│   └── analisis_visualizaciones.ipynb

├── scripts/
│   ├── scraping.py
│   └── limpieza.py

├── README.md

└── requirements.txt

---

## ✨ Principales hallazgos

- La mayoría de los productos más populares comparten **familias olfativas similares**, destacando las **orientales, florales y amaderadas**.
- Las marcas más reconocidas tienden a repetir patrones de notas en sus fragancias top.
- Existe una clara diferencia en precio entre presentaciones pequeñas y grandes, aunque muchas veces comparten fórmulas.
- Las fragancias unisex están ganando terreno, pero siguen siendo minoría.

---

## 🚀 Próximos pasos

- Clasificación de productos mediante machine learning según perfil aromático.
- Clustering para segmentar marcas o productos similares.
- Dashboard interactivo para exploración de métricas.

---

**Desarrollado por:** Daniel Lladó
📍 *Analista de Datos Junior | Apasionado por los datos, las fragancias y la visualización*

