from game import GuessNumberGame
from player import Player, save_high_scores , load_high_scores


def play_game():
    player_name = input("Enter your name : ")
    player = Player(player_name)
    load_high_scores(player)
    lower_limit = 1
    upper_limit = 100
    difficulty_levels={"easy":(1,50),"medium":(1,100),"hard":(1,150)}

    while True:
        difficulty =input("choose difficulty (easy/medium/hard) : ").lower()
        if difficulty in difficulty_levels:
            lower_limit,upper_limit =difficulty_levels[difficulty]
            break
        else:
            print("Invalid difficulty. Please choose again")

    game= GuessNumberGame(lower_limit,upper_limit)
    game.player = player
    game.generate_secret_number()

    while True:
        try:
            user_guess =int(input(f"Guess the number between {lower_limit} and {upper_limit} : "))
        except ValueError:
            print("Please Enter valid input : ")
            continue

        if game.play_round(user_guess):
            player.update_high_scores(difficulty, game.attempts)
            save_high_scores(player)
            play_again = input("Do you want to play again? (yes/no) : ")

            if play_again == "no":
                print(f" Thanks for playing ,{player.name} ! your high score is {player.high_score} ")
                return False
            else:
                game.generate_secret_number()
                game.attempts=0
          



if __name__ == "__main__":
    play_game()
