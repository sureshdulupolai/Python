from transformers import pipeline, Conversation

# Load DialoGPT model correctly
chatbot = pipeline("conversational", model="microsoft/DialoGPT-small")

print("🤖 Chatbot is ready! Type 'exit' to quit.\n")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    conversation = Conversation(user_input)
    result = chatbot(conversation)
    reply = result.generated_responses[-1]

    print(f"Bot: {reply}")
