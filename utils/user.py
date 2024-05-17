import json


class User: # User class
	def __init__(self, username, password, points = 0, stages_won = 0): # __init__ method
		self.username = username
		self.password = password
		self.points = points
		self.stages_won = stages_won

	def __str__(self): # __str__ method
		return f"User({self.username}, {self.points}, {self.stages_won})"
	
	def __repr__(self): # __repr__ method
		return f"User({self.username}, {self.points}, {self.stages_won})"

	def to_dict(self): # to_dict method
		return {
			"username": self.username,
			"password": self.password,
			"points": self.points,
			"stages_won": self.stages_won
		}
	

class UserManager: # UserManager class
	def __init__(self):
		self.users = []
		self.load_users()

	def load_users(self):
		try:
			with open("users.json", "r") as file:
				users = json.load(file)
				self.users = [User(**user) for user in users]
		except FileNotFoundError:
			self.users = []
		except Exception as e:
			print("An error occurred while loading users.")
			print(e)

	def save_users(self):
		try:
			with open("users.json", "w") as file:
				users = [user.to_dict() for user in self.users]
				json.dump(users, file, indent=4)
		except Exception as e:
			print("An error occurred while saving users.")
			print(e)

	def validate_username(self, username):
		return any(user.username == username for user in self.users)
		
	def validate_password(self, username, password):
		return any(user.username == username and user.password == password for user in self.users)	
	
	def register(self):
		print("Register")
		username = input("Enter username: ")
		if self.validate_username(username):
			print("Username already exists. Please try again.")
			return
		password = input("Enter password: ")
		self.users.append(User(username, password))
		self.save_users()
		print("User registered successfully.")

	def login(self):
		print("Login")
		username = input("Enter username: ")
		password = input("Enter password: ")
		if self.validate_password(username, password):
			print("Login successful.")
		else:
			print("Invalid username or password. Please try again.")

	def show_users(self):
		for user in self.users:
			print(user)


if __name__ == "__main__":
	user_manager = UserManager()
	user_manager.register()
	user_manager.login()
	user_manager.show_users()
	user_manager.save_users()
