from utils.user_manager import UserManager
from utils.dice_game import DiceGame
from utils.user import User

def main_menu(): # Main menu function 
  while True: # While loop to keep the menu running
    print("Welcome to Dice Roll Game!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice, or leave blank to cancel: ")
    if choice  == "1":
      UserManager.register()
    elif choice == "2":
      username = UserManager.login()
      if username:
        DiceGame.menu(username)
    elif choice == "3":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__": # Main function
  main_menu() # Call the main menu function
  