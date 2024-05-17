class Score: # Score class	
	def __init__(self, username, game_id,points = 0, wins = 0): # __init__ method	
		self.username = username
		self.game_id = game_id
		self.points = points
		self.wins = wins

	def __str__(self):
		return f"Score({self.username}, {self.points}, {self.wins})"
	
	def __repr__(self):
		return f"Score({self.username}, {self.points}, {self.wins})"
	
	def to_dict(self):
		return {
			"username": self.username,
			"game_id": self.game_id,
			"points": self.points,
			"wins": self.wins
		}



	