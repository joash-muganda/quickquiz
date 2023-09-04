import random
# from flashcard import Flashcard

# class DailyChallenge:
#     def __init__(self, user):
#         self.user = user

#     def select_random_flashcards(self):
#         return random.sample(self.user.flashcards, 5)
    

import random
from flashcard import Flashcard

class DailyChallenge:
    def __init__(self, user):
        self.user = user

    def select_random_flashcards(self):
        return random.sample(self.user.flashcards, min(5, len(self.user.flashcards)))
  
