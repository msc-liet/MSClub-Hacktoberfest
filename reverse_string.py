# reverse_string.py
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
# reverse_string.py
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_string(s)

def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = [reverse_string(word) for word in words]
    return ' '.join(reversed_words)

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
    
    if is_palindrome(string):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
    
    sentence = input("Enter a sentence: ")
    print(f"Sentence with each word reversed: {reverse_words_in_sentence(sentence)}")
