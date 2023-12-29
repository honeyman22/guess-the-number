import random

class GuessNumberGame:

    def __init__(self,lower_limit,upper_limit):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.secret_number = 0
        self.attempts = 0

    def generate_secret_number(self):
        self.secret_number = random.randint(self.lower_limit,self.upper_limit)

    def play_round(self,user_guess):
        self.attempts += 1

        if user_guess == self.secret_number:
            print(f"Congratulations! You guessed the number in {self.attempts} attempts")
            return True
        elif user_guess < self.secret_number:
            print("Too Low! Try Again")
        else:
            print("Too High! Try Again")
        return False

      

