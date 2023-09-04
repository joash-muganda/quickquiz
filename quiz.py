class Quiz:
    def __init__(self, questions, correct_answers):
        self.questions = questions
        self.user_answers = []
        self.correct_answers = correct_answers

    def answer_question(self, answer):
        self.user_answers.append(answer)

    def calculate_score(self):
        return sum([1 for user_answer, correct_answer in zip(self.user_answers, self.correct_answers) if user_answer == correct_answer])
