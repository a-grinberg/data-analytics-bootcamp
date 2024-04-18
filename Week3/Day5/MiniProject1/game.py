from random import choice

class Game:
    def get_user_item(self):
        user_item = input('Enter your choice (rock(r), paper(p) or scissors(s)): ')
        return user_item
    
    def get_computer_item(self):
        return choice(['r', 'p', 's'])
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif any([user_item == 'rock' and computer_item == 's', user_item == 'p' and computer_item == 'r', user_item == 's' and computer_item == 'p']):
            return 'won'
        else:
            return 'loss'

    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        result = self.get_game_result(user, computer)
        if result == 'draw':
            print(f'You selected {user}. The computer selected {computer}. You drew!')    
        elif result == 'loss':   
            print(f'You selected {user}. The computer selected {computer}. You lose!')
        else:
            print(f'You selected {user}. The computer selected {computer}. You won!')
        return result