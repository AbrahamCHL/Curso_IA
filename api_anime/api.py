from flask import Flask, jsonify, request as req
import sqlalchemy 
import pandas as pd
from flask_mysqldb import MySQL
import re

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/anime'

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/anime', echo=False)

app = Flask(__name__)




# mysql = MySQL(app)


@app.route('/database/', methods = ['GET'])
def create_table():
    
    # Acomodando datos
    ratings = pd.read_csv('/home/supay/datos/rating.csv', encoding="ISO-8859-1")
    ratings = ratings[['user_id','anime_id','rating']]
    animes = pd.read_csv('/home/supay/datos/anime.csv', encoding="ISO-8859-1")
    animes = animes[['anime_id','name']]


    ratings = ratings.head(1167)
    data = pd.merge(animes,ratings)

    userRatings = data.pivot_table(index = ['user_id'], columns = ['anime_id'], values = 'rating')

    corrMatrix = userRatings.corr(method='pearson', min_periods=5)

    corrMatrix.to_sql('anime', con=engine,if_exists='replace')

    
    
    return 'EXITO CAREVERGA!'
    
#@app.route()