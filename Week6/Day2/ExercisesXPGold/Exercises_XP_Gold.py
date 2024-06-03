# PART 1: Authentication CLI - Login:
# Create a dictionary that contains users: each key will represent a username, and each value will represent that user’s password. Initialize this dictionary with 3 users & passwords.
# Create a loop that does the following:
# If the user inputs “exit”, break out of the loop.
# If the user inputs “login”, ask them for their username and password.
# If the user’s details exist print “you are now logged in”.
# If the user is successfully logged in, store the username in a variable called logged_in so we can track it later.
# PART 2 : Authentication CLI - Signup:
# Continuation of the Exercise Above - Authentication CLI - login

# If the user does not exist ask if they would like to sign up:
# Ask the user for a username and make sure it doesn’t exist as a key in our dictionary, if the username is not valid continue asking the user to input a username.
# Ask the user for a password. The password is the value.
# PART 3 : Database
# Replace the dictionary of users with a database table.

# Create the functionality which will allow us to read and write users to and from the database.

# Bonus: Try and encrypt the users password before storing it in the database.

users = {'User1': 'password1', 'User2': 'password2', 'User3': 'password 3'}
user_input = None
logged_in = None
while True:
    user_input = input("Input 'login' to login or 'exit' to exit: ")
    if user_input == 'exit':
        break
    elif user_input == 'login':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if username in users and password == users.get(username):
            print('you are now logged in')
            logged_in = username
            break
        elif username not in users:
            if input('Would like to sign up (y/n)? ') == 'y':
                username = input('Enter your username: ')
                users[username] = input('Enter your password: ')
                print(users)
