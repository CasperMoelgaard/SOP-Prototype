from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, prompt, answer, explanation):
        self.prompt = prompt
        self.answer = answer
        self.explanation = explanation

    @abstractmethod
    def ask(self):
        pass

    @abstractmethod
    def check_answer(self, user_answer):
        try:
            return self.options[int(user_answer)-1] == self.answer
        except (ValueError, IndexError):
            return False