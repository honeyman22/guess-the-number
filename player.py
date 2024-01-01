import json
class Player:

    def __init__(self,name):
        self.name=name
        self.high_score = {}

    def update_high_scores(self, difficulty, attempts):
        if difficulty not in self.high_scores or attempts < self.high_scores[difficulty]:
           self.high_scores[difficulty] = attempts


def save_high_scores(player):
    data_to_save ={
    "name":player.name,
    "high_scores":player.high_scores
    }

    with open('score_card.json',"w")as file:
        json.dump(data_to_save,file)


def load_high_scores(player):
    try:
        with open('score_card.json',"r") as file:
            data_loaded = json.load(file)
            player.name = data_loaded["name"]
            player.high_scores = data_loaded["high_scores"]
    except FileNotFoundError:
        pass