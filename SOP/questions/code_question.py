from .question import Question

class CodeQuestion(Question):
    def ask(self):
        print(self.prompt)
        return input("Skriv dit svar her:\n")
    
    def check_answer(self, user_answer):
        return user_answer.strip() == self.answer.strip()