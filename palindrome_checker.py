# palindrome_checker.py
def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
# palindrome_checker.py
def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome_in_sentence(sentence):
    words = sentence.split()
    palindromes = [word for word in words if is_palindrome(word)]
    if palindromes:
        return max(palindromes, key=len)
    return None

def count_palindromes_in_sentence(sentence):
    words = sentence.split()
    palindrome_count = sum(1 for word in words if is_palindrome(word))
    return palindrome_count

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
    
    sentence = input("Enter a sentence: ")
    longest_palindrome = longest_palindrome_in_sentence(sentence)
    if longest_palindrome:
        print(f"Longest palindrome in the sentence: {longest_palindrome}")
    else:
        print("No palindromes found in the sentence.")
    
    palindrome_count = count_palindromes_in_sentence(sentence)
    print(f"Number of palindromes in the sentence: {palindrome_count}")
