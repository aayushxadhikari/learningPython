import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import json
import string

# Sample training data
intents = {
    "greeting": [
        {"input": "Hello", "output": "Hi, how can I assist you today?"},
        {"input": "Hi", "output": "Hello, how can I help?"},
        {"input": "Hey", "output": "Hey there! How can I assist you?"},
    ],
    "goodbye": [
        {"input": "Bye", "output": "Goodbye! Have a great day."},
        {"input": "See you later", "output": "See you! Take care."},
        {"input": "Goodbye", "output": "Goodbye! Stay safe."},
    ],
    "thanks": [
        {"input": "Thanks", "output": "You're welcome! Glad to help."},
        {"input": "Thank you", "output": "My pleasure! You're welcome."},
    ],
    "unknown": [
        {"input": "What is your name?", "output": "I am a chatbot created to assist you."},
        {"input": "What can you do?", "output": "I can answer questions and assist you with tasks."},
    ]
}

# Extract inputs and outputs
inputs = []
outputs = []
labels = []

for intent, examples in intents.items():
    for example in examples:
        inputs.append(example["input"])
        outputs.append(example["output"])
        labels.append(intent)

# Build a simple text classification model using Naive Bayes
nltk.download('punkt')

class Chatbot:
    def __init__(self):
        self.model = make_pipeline(CountVectorizer(), MultinomialNB())
        self.model.fit(inputs, labels)

    def clean_input(self, text):
        # Remove punctuation and convert to lowercase
        return text.translate(str.maketrans('', '', string.punctuation)).lower()

    def respond(self, user_input):
        user_input = self.clean_input(user_input)
        predicted_label = self.model.predict([user_input])[0]
        
        # Get a response based on the predicted label
        possible_responses = [example["output"] for example in intents[predicted_label]]
        return random.choice(possible_responses)

# Create chatbot instance
chatbot = Chatbot()

def chat():
    print("Chatbot: Hello! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chat()
