QuickQuiz: An Interactive Flashcard and Quiz Application nenerated by Gpt-Engineer
QuickQuiz is a console-based application that allows users to create flashcards, categorize them, generate quizzes, and track performance. It offers a daily challenge feature where users are quizzed on a random set of flashcards.

Features
Flashcard Creation: Users can create flashcards with terms/questions and their corresponding definitions/answers.
Categories: Flashcards can be grouped into categories for more organized study.
Quizzes: Users can generate quizzes based on their flashcards and test their knowledge.
Performance Tracking: After taking a quiz, users can view their score and areas of improvement.
Daily Challenge: Users are presented with a random set of flashcards daily for quick testing.


The core classes, functions, and methods that will be necessary for this application are:

1. Flashcard: This class will represent a flashcard, with attributes for the term/question and definition/answer.
2. Category: This class will represent a category, with an attribute for the category name and a list of flashcards that belong to the category.
3. Quiz: This class will represent a quiz, with attributes for the list of questions, the user's answers, and the correct answers.
4. User: This class will represent a user, with attributes for the user's name, list of flashcards, list of categories, and list of quizzes.
5. PerformanceTracker: This class will track the user's performance, with methods to calculate the score and highlight areas for improvement.
6. DailyChallenge: This class will represent the daily challenge, with a method to select random flashcards.

Getting Started

Prerequisites
Python 3.x

Installation
Clone the repository:

git clone https://github.com/joash-muganda/QuickQuiz.git


Navigate to the project directory:

cd QuickQuiz


Run the application:

python main.py


Usage
After launching the application:

Follow the on-screen prompts to create flashcards.
Opt to generate a quiz and answer the quiz questions.
View your performance and areas of improvement.
Engage with the daily challenge for a random set of flashcard questions.
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License:
None