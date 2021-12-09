
import requests as rq
import pandas as pd

df_mundiales=pd.read_csv("/content/drive/MyDrive/ESPECIALIZACIONES/PYTHON/world_cups.csv")
df_mundiales=pd.read_csv("/content/drive/MyDrive/ESPECIALIZACIONES/PYTHON/world_cups.csv",sep="\t")
#excel indicar la hoja
df1=pd.read_excel("/content/drive/MyDrive/ESPECIALIZACIONES/PYTHON/world_cups.xlsx",sheet_name="world_cups")
df_mundiales.head()

#Metodo web scraping
url_data="https://es.wikipedia.org/wiki/Mascota_de_la_Copa_Mundial_de_F%C3%BAtbol"
html_text=rq.get(url_data).content
content=pd.read_html(html_text)
content[0]

#copia y pegar
pandas.read_clipboard()

