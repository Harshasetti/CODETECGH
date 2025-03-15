from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot("AI Assistant")

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # Using the built-in English dataset

print("Chatbot is ready! Type 'exit' to end the chat.")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print(f"Chatbot: {response}")
