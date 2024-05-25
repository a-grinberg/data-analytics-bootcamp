# Daily Challenge : Web API To DB
# 1. Using this REST Countries API, create the functionality which will write 10 random countries to your database.

# 2. These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import psycopg2
import requests
import random

HOSTNAME = 'localhost'
USERNAME = 'your_username'
PASSWORD = 'your_password'
DATABASE = 'your_db'


def get_country_list():
    countries = requests.get('https://restcountries.com/v3.1/all')
    countries = countries.json()
    coutries_list = []
    for country in  countries:
        coutries_list.append((country.get('name')['common'], country.get('capital')[0] if isinstance(country.get('capital'), list)else None, country.get('flag'), country.get('subregion'), country.get('population')))
    random.shuffle(coutries_list)
    return coutries_list[:10]

countries = get_country_list()
query = "INSERT INTO country(name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s);"
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()
for country in countries:
    cursor.execute(query, country)
cursor.execute("SELECT * FROM country;")
cursor.fetchone()
connection.commit()
cursor.close()
connection.close()