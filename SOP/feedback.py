class FeedbackSystem:
    @staticmethod
    def correct():
        print("Korrekt! Godt klaret.")

    @staticmethod
    def incorrect(correct_answer):
        print(f"Forkert. Det rigtige svar er: {correct_answer}")