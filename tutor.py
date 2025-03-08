import pandas as pd
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", device=-1)  # Open, easy model
flashcards = pd.read_csv("data/flashcards.csv")

def teach_lesson(prompt):
    if "flashcard" in prompt.lower():
        card = flashcards.sample(1).iloc[0]
        return f"Thai: {card['thai']} - English: {card['english']}"
    with open("data/menu.txt") as f:
        return f"Menu item: {f.readline().strip()}"

if __name__ == "__main__":
    print(teach_lesson("Show me a flashcard"))
