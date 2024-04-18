from game import Game
def get_user_menu_choice():
    users_choice = input("'g' for play a new game \n 'x' for show scores and exit ")
    return users_choice

def print_results(results):
    for k, v in results.items():
        print(f"You {k} {v} times!")
    print( 'Thank you for playing')

def main():
    users_choice = get_user_menu_choice()
    results = {'won': 0, 'loss': 0, 'draw': 0}
    while users_choice != 'x':
        new_game = Game()
        results[new_game.play()] +=1
        users_choice = get_user_menu_choice()
    print_results(results)


if __name__ == '__main__':
    main()