from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot("teste")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

# Get a response to an input statement
while True:
    response = chatbot.get_response("Hello, how are you today?")
    print(response)