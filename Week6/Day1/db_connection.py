import psycopg2
from fake2db import Fake2DB

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'grinberg'
DATABASE = 'postgresql_fucdrtta'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()
query = "SELECT * FROM customer LIMIT 20;"
cursor.execute(query)
results = cursor.fetchall()
connection.close()
for item in results:
        print(item)
