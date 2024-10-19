def greet(language="en"):
    greetings = {
        "en": "Hello, Hacktoberfest!",
        "es": "¡Hola, Hacktoberfest!",
        "fr": "Bonjour, Hacktoberfest!",
        "de": "Hallo, Hacktoberfest!",
        "it": "Ciao, Hacktoberfest!",
    }
    return greetings.get(language, greetings["en"])  # Default to English if language not found

def main():
    print("Welcome to the Greeting Program!")
    print("Choose a language for your greeting:")
    print("1. English (en)")
    print("2. Spanish (es)")
    print("3. French (fr)")
    print("4. German (de)")
    print("5. Italian (it)")
    
    choice = input("Enter the number corresponding to your choice: ")

    language_map = {
        "1": "en",
        "2": "es",
        "3": "fr",
        "4": "de",
        "5": "it"
    }

    selected_language = language_map.get(choice, "en")  # Default to English if invalid choice

    greeting_message = greet(selected_language)
    print(greeting_message)

if __name__ == "__main__":
    main()
