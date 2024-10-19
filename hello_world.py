# hello_world.py
# Function to generate the greeting message
def generate_greeting():
    return "Hello, Hacktoberfest!"

# Function to print the greeting message
def print_greeting(message):
    print(message)

# Main function to run the program
def greet():
    message = generate_greeting()  # Get the greeting message
    print_greeting(message)        # Print the greeting message

# Run the greet function if this file is executed as the main program
if __name__ == "__main__":
    greet()

