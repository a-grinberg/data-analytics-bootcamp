from menu_item import MenuItem
from menu_manager import MenuManager
def show_user_menu():
    while True:
        print('''
                - View an Item (V)
                - Add an Item (A)
                - Delete an Item (D)
                - Update an Item (U) 
                - Show the Menu (S)
                - Exit (E)''')
        user_input = input('What do you want to do? ')
        if user_input == 'V':
            pass
        elif user_input == 'A':
            add_item_to_menu()
        elif user_input == 'D':
            remove_item_from_menu()
        elif user_input == 'U':
            update_item_from_menu()
        elif user_input == 'S':
            show_restaurant_menu()
        elif user_input == 'E':
            break

def add_item_to_menu():
    name = input("Enter item's name: ")
    price = input("Enter item's price: ")
    item = MenuItem(name, price)
    item.save()
    print('Item was added successfully')

def remove_item_from_menu():
    name = input("Enter item's name: ")
    try:
        item_name, item_price = MenuManager.get_by_name(name)[0][1:]
        item = MenuItem(item_name, item_price)
        item.delete()   
    except:
        print('Something is wrong. There was an error')
    else:
        print('Item was deleted successfully')

def update_item_from_menu():
    name = input("Enter item's name: ")
    price = input("Enter item's price: ")
    new_name = input("Enter new name of item: ")
    new_price = input("Enter new price of item: ")
    item = MenuItem(name, price)
    try: item.update(new_name, new_price)
    except:
        print('Something is wrong. There was an error')
    else:
        print('Item was deleted successfully')

def show_restaurant_menu():
    for item in MenuManager.all_items():
        print(f'Item: {item[1]} - {item[2]}$')


if __name__ == '__main__':
    show_user_menu()