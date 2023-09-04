class PerformanceTracker:
    def __init__(self, user):
        self.user = user

    def calculate_score(self, quiz):
        return quiz.calculate_score()

    def highlight_areas_for_improvement(self, quiz):
        incorrect_answers = [question for question, user_answer, correct_answer in zip(quiz.questions, quiz.user_answers, quiz.correct_answers) if user_answer != correct_answer]
        return incorrect_answers
