# count_vowels.py
def count_vowels(s, case_sensitive=False):
    vowels = "aeiou"
    if not case_sensitive:
        s = s.lower()
    count = {v: 0 for v in vowels}

    for char in s:
        if char in count:
            count[char] += 1
    
    total_vowels = sum(count.values())
    return total_vowels, count

if __name__ == "__main__":
    string = input("Enter a string: ")
    case_sensitive = input("Count vowels case sensitively? (yes/no): ").strip().lower() == 'yes'
    
    total, count = count_vowels(string, case_sensitive)
    
    print(f"Total number of vowels in '{string}': {total}")
    print("Count for each vowel:", {v: count[v] for v in count if count[v] > 0})
