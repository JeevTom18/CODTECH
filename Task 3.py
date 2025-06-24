import nltk
import random
import string
from nltk.chat.util import reflections
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

# Sample responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing fine!", "Doing great, thanks!"],
    "what is your name": ["I'm CodBot, your Python internship assistant!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"]
}

# Clean and preprocess user input
def preprocess(user_input):
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return " ".join(tokens)

# Generate response
def get_response(user_input):
    processed = preprocess(user_input)
    for key in responses:
        if key in processed:
            return random.choice(responses[key])
    return "Sorry, I didn’t understand that. Can you rephrase?"

# Chat loop
print("CodBot: Hello! Ask me anything. (Type 'exit' to end)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("CodBot: Bye! Have a great day!")
        break
    reply = get_response(user_input)
    print("CodBot:", reply)
