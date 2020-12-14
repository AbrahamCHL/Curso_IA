from flask import Flask, jsonify, request as req
import pandas as pd
from sqlalchemy import *

engine = create_engine('mysql+pymysql://root:password@localhost/anime', echo=False)

metadata = MetaData(bind=None)
app = Flask(__name__)

@app.route('/entrenamiento/', methods = ['GET'])
def create_table():
    
    # Acomodando datos
    ratings = pd.read_csv('/home/supay/datos/rating.csv')
    ratings = ratings[['user_id','anime_id','rating']]
    animes = pd.read_csv('/home/supay/datos/anime.csv')
    animes = animes[['anime_id','name']]
    #print(animes)
    animes = animes.head(700)
    # remplazo caracteres
    animes['name'] = animes['name'].str.replace(r'[./;&°#!:-]', '',regex=True)
    # corto las string
    animes['name'] = animes['name'].str.slice(0,64)
    # borro espacios finales
    animes.name = animes.name.str.rstrip()

    
    # Cortando la dataframe de ratings a 1167(cantidad de columnas sql)
    #ratings = ratings.head(1167)
    ratings = ratings.head(1000000)

    data = pd.merge(animes,ratings)

    # Agregramos el anime_id por que name a la hora de crear la tabla da problemas de duplicidad (64 caracteres sql)
    userRatings = data.pivot_table(index = ['user_id'], columns = ['name'], values = 'rating')

    corrMatrix = userRatings.corr(method='pearson', min_periods=5)

    # Se crea la tabla anime siempre, ya que lo remplaza siempre
    corrMatrix.to_sql('anime', con=engine,if_exists='replace')
    
    
    return 'Success!'
    
@app.route('/animes/recomendar/', methods=['GET'])

def animes_recomendados():
    anime = req.args.get('anime')
    rating = req.args.get('rating')
    rating = int(rating)

    corrMatrix = pd.read_sql_table('anime', 'mysql+pymysql://root:password@localhost/anime')  
    #print(corrMatrix)

    simCandidates = pd.Series()
    # #print(simCandidates)
    # # Recuperar las pelis similares a las calificadas
    # print(corrMatrix[anime])
    sims = corrMatrix[anime].dropna()
    # print(sims[0])
    # # Escalar la similaridad multiplicando por la calificación de la persona
    sims = sims.map(lambda x: x * rating)
    # # Añadir el puntaje a la lista de candidatos similares
    simCandidates = simCandidates.append(sims) 
    # #Mirar los resultados:
    # #print ("ordenando...")
    simCandidates.sort_values(inplace = True, ascending = False)
    #print(type(simCandidates))

    simCandidates = simCandidates.groupby(simCandidates.index).sum()
    simCandidates.sort_values(inplace = True, ascending = False)
    #print(simCandidates.head(10))

    #print(myRatings)
    filteredSims = simCandidates.drop(anime,errors='ignore')
    #print(type(filteredSims))
    print(filteredSims.head(10))
    #lista = filteredSims.keys()
    #lista = filteredSims.values.tolist()
    #print(lista)
    return jsonify({"Anime": "Nombre: "+ anime +" "+"rating: "+ str(rating)})