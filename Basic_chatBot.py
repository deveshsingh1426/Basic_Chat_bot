import nltk
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hi there! How can I assist you?']),
    (r'what is your name?', ['I am a chatbot created to help you.', 'You can call me ChatBot.']),
    (r'how are you?', ['I am doing great! How about you?', 'I am just a program, but I am here to help!']),
    (r'quit', ['Bye! Have a great day!', 'Goodbye!']),
]

def chatbot():
    print("Hello! I am a chatbot. Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        if response:
            print("ChatBot:", response)
        else:
            print("ChatBot: Sorry, I don't understand that.")

        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chatbot()
