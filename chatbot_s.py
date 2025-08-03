from turtle import hideturtle


def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there! How can I help you?")
        
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm just a bunch of code, but I'm doing fine! How about you?")
        
        elif user_input in ["what's your name", "what is your name"]:
            print("Chatbot: I'm ChatBot 1.0. You can call me Bot!")
        elif user_input in ["who is tanvi", "do you know tanvi", "you know tanvi?"]:
            print("Chatbot: chal chal chal challlllllllllll😹😁")
        elif user_input in ["you know ronaldo", "do you know ronaldo", "you know ronaldo?"]:
            print("Chatbot: Do you mean GOAT?")
        
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        elif user_input == "":
            print("Chatbot: Please say something.")
        
        else:
            print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()