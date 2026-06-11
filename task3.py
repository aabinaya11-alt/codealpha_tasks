# ============================================
# Project: Simple Rule-Based Chatbot
# Author: Internship Project
# Description: A basic chatbot that replies to
# specific user messages using if-elif-else
# ============================================

# --- Welcome message when the program starts ---
print("======================================")
print("        Welcome to Simple ChatBot!    ")
print("======================================")
print("You can talk to me! Type 'hello' to exit Type 'bye'.")
print()

# --- This loop keeps the chat going until the user types "bye" ---
while True:

    # --- Take input from the user ---
    user_input = input("You: ")

    # --- Convert input to lowercase so it works even if user types in caps ---
    # For example "Hello", "HELLO", "hello" will all be treated the same
    user_input = user_input.lower()

    # --- Remove extra spaces from the beginning and end of the input ---
    user_input = user_input.strip()

    # --- Check what the user typed and give the correct reply ---

    if user_input == "hello":
        print("ChatBot: Hi!")

    elif user_input == "how are you":
        print("ChatBot: I'm fine, thanks!")

    elif user_input == "what is your name":
        print("ChatBot: I am a simple chatbot.")

    elif user_input == "bye":
        # --- Say goodbye and stop the loop ---
        print("ChatBot: Goodbye!")
        break   # this exits the while loop and ends the program

    else:
        # --- If the input doesn't match anything, show a default message ---
        print("ChatBot: Sorry, I don't understand that.")

    # --- Print a blank line to make the chat easier to read ---
    print()
