from menu_item import MenuItem, DbConnection

class MenuManager:

    @staticmethod
    def get_by_name(name):
        query = 'SELECT * FROM Menu_Items WHERE item_name=%s;'
        return DbConnection.execute_select(query, (name,))
    
    @staticmethod
    def all_items():
        query = 'SELECT * FROM Menu_Items;'
        return DbConnection.execute_select(query)