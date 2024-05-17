from random import randint # Import the randint function from the random module

class DiceGame: # DiceGame class
    scores = [] # scores list

    def __init__(self, username): # __init__ method
        self.username = username
        self.points = 0
        self.stage = 1
        self.wins = 0


    def load_scores(): # load_scores method 
        try:
            with open("scores.txt", "r") as file:
                DiceGame.scores = [eval(line.strip()) for line in file]
        except FileNotFoundError:
            DiceGame.scores = []

    def save_scores(): # save_scores method
        with open("scores.txt", "w") as file:
            for score in DiceGame.scores:
                file.write(str(score) + '\n')

    def play_game(self): # play_game method
        while True: # While loop to keep the game running
            print(f"Starting game as {self.username} ...")
            player_wins = 0
            cpu_wins = 0
            rounds_to_win = 2

            while player_wins < rounds_to_win and cpu_wins < rounds_to_win: # While loop to keep the game running
                print(f"Stage {self.stage} Round {player_wins + cpu_wins + 1}")
                player_roll = randint(1, 6)
                cpu_roll = randint(1, 6)

                print(f"{self.username} rolled: {player_roll}")
                print(f"CPU rolled: {cpu_roll}")

                if player_roll > cpu_roll:
                    player_wins += 1
                    print(f"{self.username} wins this round.")
                elif cpu_roll > player_roll:
                    cpu_wins += 1
                    print("CPU wins this round.")
                else:
                    print("It's a tie.")

            if player_wins > cpu_wins: # If the player wins
                self.points += self.stage  # Earn points equal to the stage number
                print(f"{self.username} wins the stage!")
                print(f"Total Points: {self.points}, Stages Won: {self.stage}")
                self.save_score()
                choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                if choice == "0":
                    print(f"Game over. You won {self.stage} stage(s) with a total of {self.points} points.")
                    break
                elif choice == "1":
                    self.stage += 1
                else:
                    print("Invalid input. Please enter 1 for Yes or 0 for No.")
            else:
                print(f"You lost this stage, {self.username}")
                print("Game Over. You didn't win any stages")
                break

    def save_score(self): # save_score method
        stage_wins = self.stage - 1  # Assuming each stage won counts as one stage win
        DiceGame.scores.append({'username': self.username, 'points': self.points, 'stage_wins': stage_wins})

   
    def show_top_scores(): # show_top_scores method
        if not DiceGame.scores: # If there are no scores 
            print("No games played yet. Play a game to see top scores.")
        else:
            sorted_scores = sorted(DiceGame.scores, key=lambda x: x['points'], reverse=True) # Sort the scores in descending order
            print("Top Scores:")
            for rank,score in enumerate(sorted_scores[:10], start=1): # For loop to iterate through the scores
                print(f"{rank}. {score['username']}: Points - {score['points']}, Wins - {score['stage_wins']}")

  
    def logout(username): # logout method   
        print(f"Goodbye {username}!")
        print("You logged out successfully.")
        return

  
    def menu(username): # menu method
        game = DiceGame(username)
        while True:
            print("Welcome, " + str(username) + "!")
            print("Menu:")
            print("1. Play Game")
            print("2. Show Top Scores")
            print("3. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                game.play_game() # Call the play_game method
            elif choice == "2":
                DiceGame.show_top_scores() # Call the show_top_scores method
            elif choice == "3":
                DiceGame.logout(username) # Call the logout method
                break
            else:
                print("Invalid choice. Please try again.")