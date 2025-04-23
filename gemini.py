# # pip install google-generativeai - install
# import google.generativeai as genai

# genai.configure(api_key="AIzaSyAYvHy2v1jwGTCeaK-2Mw8vWchD8qY3NWs")
# model = genai.GenerativeModel("gemini-1.5-pro-latest")

# def AiBot(username):
#     print("Mr/Ms. {}, To Exit Type 'exit' to quit.\n".format(username))
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit", "bye"]:
#             print("Chatbot: bye! {}".format(username))
#             break

#         try:
#             response = model.generate_content(user_input)
#             print("Chatbot:", response.text)

#         except Exception as e:
#             print("❌ Error:", e)

# def Username():
#     Username = input('hi i am Ai Bot, What is Your name : ').strip().capitalize()
#     if Username:
#         AiBot(username=Username)
#     else:
#         Username()

# if __name__ == '__main__':
#     Username()
# else:
#     print('To Chat With "Ai Bot", Use File python gemini.py')