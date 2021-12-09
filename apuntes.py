
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

#dimensiones
df_mundiales.shape
out: (20, 10)
n_filas=df_mundiales.shape[0]
n_columnas=df_mundiales.shape[1]

#informacion de la estructura
df_mundiales.info()
out:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 20 entries, 0 to 19
    Data columns (total 10 columns):
     #   Column          Non-Null Count  Dtype 
    ---  ------          --------------  ----- 
     0   Year            20 non-null     int64 
     1   Country         20 non-null     object
     2   Winner          20 non-null     object
     3   Runners-Up      20 non-null     object
     4   Third           20 non-null     object
     5   Fourth          20 non-null     object
     6   GoalsScored     20 non-null     int64 
     7   QualifiedTeams  20 non-null     int64 
     8   MatchesPlayed   20 non-null     int64 
     9   Attendance      20 non-null     object
    dtypes: int64(4), object(6)
    memory usage: 1.7+ KB
  
