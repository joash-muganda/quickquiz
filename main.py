
import random
from user import User
from performance_tracker import PerformanceTracker
from daily_challenge import DailyChallenge

def main():
    user = User("John Doe")
    performance_tracker = PerformanceTracker(user)

    # User input for creating flashcards
    while True:
        term = input("Enter the term/question for the flashcard (or 'exit' to stop): ")
        if term.lower() == 'exit':
            break
        definition = input("Enter the definition/answer for the flashcard: ")
        flashcard = user.create_flashcard(term, definition)
        
        # User input for category assignment
        print("\nCategories:")
        for idx, category in enumerate(user.categories, 1):
            print(f"{idx}. {category.name}")
        category_choice = input("Select a category number or 'new' to create a new category: ")
        if category_choice.lower() == 'new':
            category_name = input("Enter the name for the new category: ")
            category = user.create_category(category_name)
        else:
            category = user.categories[int(category_choice) - 1]
        category.add_flashcard(flashcard)

    # User input for quiz generation
    generate_quiz = input("Do you want to generate a quiz? (yes/no): ").lower()
    if generate_quiz == 'yes':
        num_questions = int(input("How many questions do you want in the quiz? "))
        flashcards_for_quiz = random.sample(user.flashcards, min(num_questions, len(user.flashcards)))
        
        questions = [flashcard.term for flashcard in flashcards_for_quiz]
        correct_answers = [flashcard.definition for flashcard in flashcards_for_quiz]
        
        quiz = user.create_quiz(questions, correct_answers)
        
        for question in questions:
            answer = input(f"Question: {question} ")
            quiz.answer_question(answer)

        print("Quiz score:", performance_tracker.calculate_score(quiz))
        print("Areas for improvement:", performance_tracker.highlight_areas_for_improvement(quiz))

if __name__ == "__main__":
    main()
