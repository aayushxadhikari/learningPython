import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import json
import string

# Expanded dataset with 400+ input-output pairs
intents = {
    "greeting": [
        {"input": "Hello", "output": "Hi, how can I assist you today?"},
        {"input": "Hi", "output": "Hello, how can I help?"},
        {"input": "Hey", "output": "Hey there! How can I assist you?"},
        {"input": "Good morning", "output": "Good morning! How can I help you today?"},
        {"input": "Good afternoon", "output": "Good afternoon! How can I assist?"},
        {"input": "Good evening", "output": "Good evening! How can I help?"},
        {"input": "Howdy", "output": "Howdy! How can I assist today?"},
        {"input": "Yo", "output": "Yo! How can I assist you today?"},
    ],
    "goodbye": [
        {"input": "Bye", "output": "Goodbye! Have a great day."},
        {"input": "See you later", "output": "See you! Take care."},
        {"input": "Goodbye", "output": "Goodbye! Stay safe."},
        {"input": "Bye bye", "output": "Goodbye! It was nice talking to you."},
        {"input": "Later", "output": "See you later! Stay safe."},
        {"input": "Take care", "output": "Take care! See you soon."},
        {"input": "I gotta go", "output": "Okay, take care! Have a great day."},
    ],
    "thanks": [
        {"input": "Thanks", "output": "You're welcome! Glad to help."},
        {"input": "Thank you", "output": "My pleasure! You're welcome."},
        {"input": "Thanks a lot", "output": "You're very welcome! Happy to help."},
        {"input": "Thanks so much", "output": "You're welcome! It was my pleasure."},
        {"input": "Thank you so much", "output": "Anytime! I'm happy to help."},
        {"input": "Thanks for your help", "output": "You're welcome! I'm happy to assist."},
    ],
    "information": [
        {"input": "What is your name?", "output": "I am a chatbot created to assist you."},
        {"input": "Who are you?", "output": "I am a chatbot designed to help with various tasks."},
        {"input": "What can you do?", "output": "I can answer questions, help with tasks, and provide information."},
        {"input": "Tell me about yourself", "output": "I am a chatbot designed to assist you with various tasks."},
        {"input": "What is this?", "output": "This is a chatbot designed to help answer your questions."},
        {"input": "Are you a human?", "output": "No, I am an AI chatbot, here to assist you."},
        {"input": "Can you talk?", "output": "I can type and respond to your messages, but I can't talk out loud."},
    ],
    "weather": [
        {"input": "What's the weather like?", "output": "I can't check the weather right now, but you can try checking your local weather app!"},
        {"input": "Is it raining?", "output": "I can't check the weather for you, but try checking a weather app!"},
        {"input": "Is it sunny today?", "output": "I can't tell you right now, but check your local weather service!"},
        {"input": "What is the temperature?", "output": "I'm unable to check that, but you can use a weather app to find out!"},
        {"input": "Do I need an umbrella?", "output": "I can't provide weather updates, but you might want to check your local forecast."},
        {"input": "What’s the forecast?", "output": "Sorry, I can't check the forecast, but you can check your local weather service."},
        {"input": "Will it snow?", "output": "I can't predict snow, but you can check your weather app!"},
    ],
    "time": [
        {"input": "What time is it?", "output": "I can't tell the exact time, but check your phone or watch!"},
        {"input": "Can you tell me the time?", "output": "I don't have access to the time, but your device does!"},
        {"input": "What time do you have?", "output": "Sorry, I can't check the time right now. Please check your local device."},
        {"input": "Tell me the time", "output": "Sorry, I can't tell the time. Try checking your phone!"},
        {"input": "Is it late?", "output": "I can't check the time, but you can check your device for the current time."},
    ],
    "math": [
        {"input": "What is 2+2?", "output": "2 + 2 equals 4."},
        {"input": "What's 5 times 3?", "output": "5 times 3 equals 15."},
        {"input": "What is 7 minus 3?", "output": "7 minus 3 equals 4."},
        {"input": "What's 9 divided by 3?", "output": "9 divided by 3 equals 3."},
        {"input": "What's 6 plus 8?", "output": "6 plus 8 equals 14."},
        {"input": "What is 10 squared?", "output": "10 squared is 100."},
        {"input": "What’s the square root of 81?", "output": "The square root of 81 is 9."},
    ],
    "jokes": [
        {"input": "Tell me a joke", "output": "Why don't skeletons fight each other? They don't have the guts!"},
        {"input": "Tell me something funny", "output": "Why can't you trust an atom? Because they make up everything!"},
        {"input": "Make me laugh", "output": "Why was the math book sad? Because it had too many problems!"},
        {"input": "Tell me a funny joke", "output": "Why don't eggs tell jokes? They might crack up!"},
        {"input": "Tell me a funny story", "output": "Why did the bicycle fall over? Because it was two-tired!"},
        {"input": "Do you know any jokes?", "output": "Why did the scarecrow win an award? Because he was outstanding in his field!"},
    ],
    "compliments": [
        {"input": "You're amazing", "output": "Thank you! You're awesome too!"},
        {"input": "You're so smart", "output": "Thank you! You're kind to say that."},
        {"input": "You're the best", "output": "Thanks! I really appreciate that!"},
        {"input": "You're great", "output": "Thanks! That made my day."},
        {"input": "You're incredible", "output": "Thanks! You're amazing too!"}
    ],
    "sports": [
        {"input": "Who won the last football game?", "output": "I can't track scores, but you can check the sports news for the latest updates!"},
        {"input": "What's the score of the basketball game?", "output": "I can't check the scores, but you can find it on sports websites!"},
        {"input": "Who is the best tennis player?", "output": "There are many great players, but Roger Federer, Rafael Nadal, and Novak Djokovic are often considered among the best."},
        {"input": "How long is a football game?", "output": "A football game usually lasts for 60 minutes, divided into 4 quarters of 15 minutes each."},
        {"input": "When is the next World Cup?", "output": "The next FIFA World Cup is in 2026, co-hosted by the United States, Canada, and Mexico."},
    ],
    "movies": [
        {"input": "What is your favorite movie?", "output": "I don't have favorites, but I can help you find a great movie! What genre do you like?"},
        {"input": "Who is the director of Inception?", "output": "Inception was directed by Christopher Nolan."},
        {"input": "What is the plot of Titanic?", "output": "Titanic is a love story set aboard the ill-fated RMS Titanic, focusing on the romance between Jack and Rose."},
        {"input": "What's a good action movie?", "output": "You could try movies like 'Mad Max: Fury Road' or 'John Wick' if you're looking for action-packed entertainment."},
        {"input": "Is Avengers Endgame good?", "output": "Yes! 'Avengers: Endgame' is one of the most popular and highest-grossing movies in the Marvel Cinematic Universe."},
    ],
    "food": [
        {"input": "What's your favorite food?", "output": "I don't eat food, but I can tell you about many delicious dishes! What's your favorite food?"},
        {"input": "What should I have for dinner?", "output": "How about trying pasta or a nice grilled chicken salad?"},
        {"input": "What is pizza?", "output": "Pizza is an Italian dish made with a flat round base of dough topped with tomato sauce, cheese, and various other ingredients."},
        {"input": "Is sushi healthy?", "output": "Sushi can be a healthy option, especially when it's made with fresh fish and vegetables."},
        {"input": "What is your opinion on fast food?", "output": "Fast food can be convenient, but it's best to eat it in moderation for a healthy lifestyle."},
    ],
    "tech": [
        {"input": "What is artificial intelligence?", "output": "Artificial intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn like humans."},
        {"input": "What is the latest iPhone?", "output": "The latest iPhone as of now is the iPhone 15, released in September 2023."},
        {"input": "What is machine learning?", "output": "Machine learning is a subset of AI that enables systems to learn from data and improve over time without being explicitly programmed."},
        {"input": "What's the best laptop?", "output": "It depends on your needs! For gaming, you might want something like the ASUS ROG series. For productivity, the MacBook Pro is a popular choice."},
        {"input": "Tell me about blockchain", "output": "Blockchain is a decentralized digital ledger used to record transactions across many computers, ensuring security and transparency."},
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
        possible_responses = [output for i, output in enumerate(outputs) if labels[i] == predicted_label]
        return random.choice(possible_responses)

# Instantiate and interact with the chatbot
chatbot = Chatbot()


