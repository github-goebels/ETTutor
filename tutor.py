import pandas as pd
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", device=-1)
flashcards = pd.read_csv("data/flashcards.csv")

def teach_lesson(prompt):
    if "flashcard" in prompt.lower():
        card = flashcards.sample(1).iloc[0]
        return f"Thai: {card['thai']} - English: {card['english']}"
    if "menu" in prompt.lower():
        with open("data/menu.txt") as f:
            return f"Menu item: {f.readline().strip()}"
    return "Try asking for a 'flashcard' or 'menu'!"

if __name__ == "__main__":
    print("Welcome to ETTutor! Type 'exit' to quit.")
    while True:
        prompt = input("What would you like to learn? ")
        if prompt.lower() == "exit":
            print("Goodbye!")
            break
        print(teach_lesson(prompt))
