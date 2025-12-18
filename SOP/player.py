class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.level = 1

    def add_score(self, points):
        self.score += points
    
    def level_up(self):
        self.level += 1