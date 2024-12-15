# hello_world.py
def greet():
    print("Hello, Hacktoberfest!")

if __name__ == "__main__":
    greet()
def greet():
    print("Hello, Hacktoberfest!")

def greet_person(name):
    print(f"Hello, {name}! Welcome to Hacktoberfest!")

def shout_greeting():
    print("HELLO, HACKTOBERFEST!!!")

def greet_in_language(language):
    greetings = {
        "english": "Hello, Hacktoberfest!",
        "spanish": "¡Hola, Hacktoberfest!",
        "french": "Bonjour, Hacktoberfest!",
        "german": "Hallo, Hacktoberfest!",
        "italian": "Ciao, Hacktoberfest!"
    }
    
    # Default to English if the language is not found
