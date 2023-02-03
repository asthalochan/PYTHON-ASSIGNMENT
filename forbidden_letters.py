import random

# List of forbidden characters
forbidden = ['a', 'e', 'i', 'o', 'u']

# The word to guess
word = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 6))

# Number of attempts allowed
attempts = 10

for i in range(attempts):
    guess = input("Enter a word (6 letters): ")
    forbidden_count = sum(c in forbidden for c in guess)
    if forbidden_count == 0:
        print("Congratulations! You guessed the word.")
        break
    else:
        print("Your guess contains", forbidden_count, "forbidden character(s).")
else:
    print("Sorry, you didn't guess the word. The word was: ", word)
