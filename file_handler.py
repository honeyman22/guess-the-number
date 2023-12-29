import json

def save_high_scores(player):
    data_to_save ={
        "name":player.name,
        "high_score":player.high_score
    }

    with open('score_card.json',"w")as file:
        json.dump(data_to_save,file)


def load_high_score(player):
    try:
        with open('score_card.json',"r") as file:
            data_loaded = json.load(file)
            player.name = data_loaded["name"]
            player.high_scores = data_loaded["high_scores"]
    except FileNotFoundError:
        pass