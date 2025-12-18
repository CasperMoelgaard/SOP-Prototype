from player import Player
from feedback import FeedbackSystem
from save_manager import SaveManager
from state import GameState
from questions.multiple_choice import MultipleChoiceQuestion
from questions.code_question import CodeQuestion

class Game:
    def __init__(self):
        self.state = GameState.MENU
        self.player = None
        self.questions = self.load_questions()
    
    def load_questions(self):
        return [
            MultipleChoiceQuestion(
                prompt="Hvad er hovedstaden i Danmark?",
                options=["København", "Aarhus", "Odense", "Aalborg"],
                answer="København",
                explanation="København er hovedstaden i Danmark."
            ),
            CodeQuestion(
                prompt="Skriv en funktion i Python, der returnerer summen af to tal.",
                answer="def sum(a, b): return a + b",
                explanation="Funktionen tager to argumenter og returnerer deres sum."
            )
        ]
    
    def run(self):
        while self.state != GameState.EXIT:
            if self.state == GameState.MENU:
                self.menu()
            elif self.state == GameState.PLAYING:
                self.play_game()
    
    def menu(self):
        print("1. Start Spil")
        print("2. afslut")
        choice = input("> ")

        if choice == "1":
            name = input("Indtast dit navn: ")
            self.player = Player(name)
            save = SaveManager.load()
            if save and save['name'] == name:
                self.player.score = save['score']
                self.player.level = save['level']
            self.state = GameState.PLAYING
        else:
            self.state = GameState.EXIT
    
    def play_game(self):
        for q in self.questions:
            answer = q.ask()
            if q.check_answer(answer):
                FeedbackSystem.correct()
                self.player.score += 10 
            else:
                FeedbackSystem.incorrect(q.answer)
        SaveManager.save(self.player)
        self.state = GameState.MENU