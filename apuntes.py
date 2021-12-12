
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
 #Muestra la descripcion de variables numericas
df_mundiales.describe()
out:
    Year	GoalsScored	QualifiedTeams	MatchesPlayed
    count	20.000000	20.000000	20.000000	20.000000
    mean	1974.800000	118.950000	21.250000	41.800000
    std	25.582889	32.972836	7.268352	17.218717
    min	1930.000000	70.000000	13.000000	17.000000
    25%	1957.000000	89.000000	16.000000	30.500000
    50%	1976.000000	120.500000	16.000000	38.000000
    75%	1995.000000	145.250000	26.000000	55.000000
    max	2014.000000	171.000000	32.000000	64.000000
  
EXPLORACION II

#Paises que fueron campeones de locales

df_mundiales[df_mundiales["Country"]==df_mundiales["Winner"]]

#mundiales en que se anotaron mas goles

df_mundiales.sort_values(by="GoalsScored",ascending=False)

#series

winner=df_mundiales["Winner"]
winner
Out:
    0        Uruguay
    1          Italy
    2          Italy
    3        Uruguay
    4     Germany FR
    5         Brazil
    6         Brazil
    7        England
    8         Brazil
    9     Germany FR
    10     Argentina
    11         Italy
    12     Argentina
    13    Germany FR
    14        Brazil
    15        France
    16        Brazil
    17         Italy
    18         Spain
    19       Germany
    Name: Winner, dtype: object
 type(winner)
pandas.core.series.Series


winner.value_counts()

Brazil        5
Italy         4
Germany FR    3
Argentina     2
Uruguay       2
England       1
France        1
Spain         1
Germany       1
Name: Winner, dtype: int64

        
        

