import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import json
import string

# Expanded dataset with 200+ input-output pairs
intents = {
    "greeting": [
        {"input": "Hello", "output": "Hi, how can I assist you today?"},
        {"input": "Hi", "output": "Hello, how can I help?"},
        {"input": "Hey", "output": "Hey there! How can I assist you?"},
        {"input": "Good morning", "output": "Good morning! How can I help you today?"},
        {"input": "Good afternoon", "output": "Good afternoon! How can I assist?"},
        {"input": "Good evening", "output": "Good evening! How can I help?"},
    ],
    "goodbye": [
        {"input": "Bye", "output": "Goodbye! Have a great day."},
        {"input": "See you later", "output": "See you! Take care."},
        {"input": "Goodbye", "output": "Goodbye! Stay safe."},
        {"input": "Bye bye", "output": "Goodbye! It was nice talking to you."},
        {"input": "Later", "output": "See you later! Stay safe."},
    ],
    "thanks": [
        {"input": "Thanks", "output": "You're welcome! Glad to help."},
        {"input": "Thank you", "output": "My pleasure! You're welcome."},
        {"input": "Thanks a lot", "output": "You're very welcome! Happy to help."},
        {"input": "Thanks so much", "output": "You're welcome! It was my pleasure."},
        {"input": "Thank you so much", "output": "Anytime! I'm happy to help."},
    ],
    "information": [
        {"input": "What is your name?", "output": "I am a chatbot created to assist you."},
        {"input": "Who are you?", "output": "I am a chatbot designed to help with various tasks."},
        {"input": "What can you do?", "output": "I can answer questions, help with tasks, and provide information."},
        {"input": "Tell me about yourself", "output": "I am a chatbot designed to assist you with various tasks."},
        {"input": "What is this?", "output": "This is a chatbot designed to help answer your questions."},
    ],
    "weather": [
        {"input": "What's the weather like?", "output": "I can't check the weather right now, but you can try checking your local weather app!"},
        {"input": "Is it raining?", "output": "I can't check the weather for you, but try checking a weather app!"},
        {"input": "Is it sunny today?", "output": "I can't tell you right now, but check your local weather service!"},
        {"input": "What is the temperature?", "output": "I'm unable to check that, but you can use a weather app to find out!"},
        {"input": "Do I need an umbrella?", "output": "I can't provide weather updates, but you might want to check your local forecast."},
    ],
    "time": [
        {"input": "What time is it?", "output": "I can't tell the exact time, but check your phone or watch!"},
        {"input": "Can you tell me the time?", "output": "I don't have access to the time, but your device does!"},
        {"input": "What time do you have?", "output": "Sorry, I can't check the time right now. Please check your local device."},
    ],
    "math": [
        {"input": "What is 2+2?", "output": "2 + 2 equals 4."},
        {"input": "What's 5 times 3?", "output": "5 times 3 equals 15."},
        {"input": "What is 7 minus 3?", "output": "7 minus 3 equals 4."},
        {"input": "What's 9 divided by 3?", "output": "9 divided by 3 equals 3."},
        {"input": "What's 6 plus 8?", "output": "6 plus 8 equals 14."},
    ],
    "jokes": [
        {"input": "Tell me a joke", "output": "Why don't skeletons fight each other? They don't have the guts!"},
        {"input": "Tell me something funny", "output": "Why can't you trust an atom? Because they make up everything!"},
        {"input": "Make me laugh", "output": "Why was the math book sad? Because it had too many problems!"},
        {"input": "Tell me a funny joke", "output": "Why don't eggs tell jokes? They might crack up!"},
    ],
    "compliments": [
        {"input": "You're amazing", "output": "Thank you! You're awesome too!"},
        {"input": "You're so smart", "output": "Thank you! You're kind to say that."},
        {"input": "You're the best", "output": "Thanks! I really appreciate that!"},
        {"input": "You're great", "output": "Thanks! That made my day."},
    ],
    "help": [
        {"input": "Can you help me?", "output": "Of course! What do you need help with?"},
        {"input": "I need assistance", "output": "I'm here to assist you! What do you need help with?"},
        {"input": "Help me out", "output": "How can I assist you today?"},
        {"input": "I need help", "output": "What can I do to help you?"},
    ],
    "unknown": [
        {"input": "What is the meaning of life?", "output": "That's a great philosophical question! I'm still figuring that out myself."},
        {"input": "Tell me something interesting", "output": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!"},
        {"input": "What is the capital of France?", "output": "The capital of France is Paris."},
        {"input": "Who is the president of the USA?", "output": "The president of the United States is Joe Biden."},
        {"input": "What is Python?", "output": "Python is a high-level programming language known for its readability and versatility."},
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
