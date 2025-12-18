import json 
import os

class SaveManager:
    SAVE_FILE = "savegame.json"

    @staticmethod
    def save(player):
        data = {
            "name": player.name,
            "score": player.score,
            "level": player.level
        }
        with open(SaveManager.SAVE_FILE, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load():
        if not os.path.exists(SaveManager.SAVE_FILE):
            return None
        with open(SaveManager.SAVE_FILE, 'r') as f:
            data = json.load(f)
        return data