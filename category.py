class Category:
    def __init__(self, name):
        self.name = name
        self.flashcards = []

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)
