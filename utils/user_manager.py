from utils.user import User # User class
from utils.dice_game import DiceGame # DiceGame class

class UserManager: # UserManager class
	users = [] # users list
	def load_users(): # load_users method
		try: 
			with open("users.txt", "r") as file: # Open the users.txt file in read mode
				UserManager.users = [eval(line.strip()) for line in file]
		except FileNotFoundError:
			UserManager.users = []


	def save_users(): # save_users method
		with open("users.txt", "w") as file: # Open the users.txt file in write mode
			for user in UserManager.users:
				file.write(str(user) + '\n')


	def validate_username(username): # validate_username method
		for user in UserManager.users:
			if user.username == username:
				return True
		

	def validate_password(username, password): # validate_password method
		for user in UserManager.users:
			if user.username == username and user.password == password:
				return True
	

	def register(): # register method
		print("Registering...")
		username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
		password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
		if len(username) < 4 or len(password) < 8: # If the length of the username is less than 4 or the length of the password is less than 8
			print("Username must be at least 4 characters long and password must be at least 8 characters long.")
			return
		if UserManager.validate_username(username):
			print("Username already exists. Please try again.")
			return
		user = User(username, password)
		UserManager.users.append(user)
		UserManager.save_users()
		print("Registration Successful.")

	def login(): # login method
		print("Login")
		username = input("Enter username, or leave blank to cancel:")
		password = input("Enter password, or leave blank to cancel:")
		if UserManager.validate_password(username, password):
			print("Login successful.")
			DiceGame.menu(username)
		else:
			print("Invalid username or password. Please try again.")

		


	