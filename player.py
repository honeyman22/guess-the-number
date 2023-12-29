class Player:

    def __init__(self,name):
        self.name=name
        self.high_score = 0

    def update_high_score(self,attempts):
        if attempts < 11 :
            self.high_score += 10/attempts
        else:
            self.high_score -= 5