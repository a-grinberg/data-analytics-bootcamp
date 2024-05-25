import psycopg2

class DbConnection:
    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = 'grinberg'
    DATABASE = 'W6D2_ex'

    @staticmethod
    def execute_change(query, values):
        connection = psycopg2.connect(host=__class__.HOSTNAME,
                                    user=__class__.USERNAME,
                                    password=__class__.PASSWORD,
                                    dbname=__class__.DATABASE )
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        connection.close()
    
    @staticmethod
    def execute_select(query, values=None):
        connection = psycopg2.connect(host=__class__.HOSTNAME,
                                    user=__class__.USERNAME,
                                    password=__class__.PASSWORD,
                                    dbname=__class__.DATABASE )
        cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        return results

class MenuItem:
    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = 'grinberg'
    DATABASE = 'W6D2_ex'

    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        query = 'INSERT INTO Menu_Items  (item_name, item_price) VALUES (%s, %s);'
        values = (self.item_name, self.item_price)
        DbConnection.execute_change(query, values)

    def delete(self):
        query = 'DELETE FROM Menu_Items WHERE item_name=%s;'
        DbConnection.execute_change(query, (self.item_name,))

    def update(self, item_name, item_price):
        query = 'UPDATE Menu_Items SET item_name=%s, item_price=%s WHERE item_name=%s'
        values = (item_name, item_price, self.item_name)
        DbConnection.execute_change(query, values)
        self.item_name = item_name
        self.item_price = item_price