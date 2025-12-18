from questions.question import Question


class MultipleChoiceQuestion(Question):
	def __init__(self, prompt, options, answer, explanation):
		super().__init__(prompt, answer, explanation)
		self.options = options

	def ask(self):
		print(self.prompt)
		for i, option in enumerate(self.options):
			print(f"{i+1}. {option}")
		return input("Svar (1-4): ")

	def check_answer(self, user_answer):
		return self.options[int(user_answer)-1] == self.answer