from collections import Counter
import string

def analyze_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra whitespace and split into words
    words = text.strip().split()

    # Total word count
    total_words = len(words)

    # Frequency table
    frequency = Counter(words)

    # Find palindromes
    palindromes = sorted(set(word for word in words if len(word) > 1 and word == word[::-1]))

    # Display report
    print("\n===== TEXT ANALYSIS REPORT =====")
    print("Total Words:", total_words)

    print("\nPalindromic Words:")
    if palindromes:
        for word in palindromes:
            print("-", word)
    else:
        print("No palindromes found.")

    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(f"{word}: {count}")


# Choose input method
print("1. Enter text manually")
print("2. Read text from a file")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    print("\nEnter your text (press Enter twice to finish):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    analyze_text(text)

elif choice == "2":
    filename = input("Enter file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        analyze_text(text)

    except FileNotFoundError:
        print("Error: File not found.")

else:
    print("Invalid choice.")