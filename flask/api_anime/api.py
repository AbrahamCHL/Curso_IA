from flask import Flask, jsonify, request as req
import sqlalchemy 
import pandas as pd
from flask_mysqldb import MySQL
from sqlalchemy import create_engine, select, MetaData, Table

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/anime'

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/anime', echo=False)
metadata = MetaData(bind=None)
app = Flask(__name__)


mysql = MySQL(app)


@app.route('/entrenamiento/', methods = ['GET'])
def create_table():
    
    # Acomodando datos
    ratings = pd.read_csv('/home/supay/datos/rating.csv')
    ratings = ratings[['user_id','anime_id','rating']]
    animes = pd.read_csv('/home/supay/datos/anime.csv')
    animes = animes[['anime_id','name']]

    # Cortando la dataframe de ratings a 1167(cantidad de columnas sql)
    ratings = ratings.head(1167)
    data = pd.merge(animes,ratings)

    # Agregramos el anime_id por que name a la hora de crear la tabla da problemas de duplicidad (64 caracteres sql)
    userRatings = data.pivot_table(index = ['user_id'], columns = ['anime_id'], values = 'rating')

    corrMatrix = userRatings.corr(method='pearson', min_periods=5)

    # Se crea la tabla anime siempre, ya que lo remplaza siempre
    corrMatrix.to_sql('anime', con=engine,if_exists='replace')

    
    return 'Success!'
    
@app.route('/animes/recomendar', methods=['GET'])

def animes_recomendados():
    #cur = mysql.connection.cursor()
    #corrMatrix = cur.execute("SELECT * FROM anime")
    #anime = int(input("ID Anime: "))
    #calificacion = int(input("Calificación: "))
    table = Table('anime', metadata, autoload = True, autoload_with = engine)
    stmt = select([table])
    """results = connection.execute(stmt).fetchall()
    for result in results:
        print(result)"""

    """sim_candidates = pd.Series()

    sims = corrMatrix[request.args['anime']].dropna()
    sims = sims.map(lambda x: x * request.args['calificacion'])
    sim_candidates = sim_candidates.append(sims)

    sim_candidates = sim_candidates.groupby(sim_candidates.index()).sum()
    sim_candidates.sort_values(inplace=True, ascending = False)
    filtered_sims = sim_candidates.drop(request.args['anime'], errors = 'ignore')"""

    return "Hola"