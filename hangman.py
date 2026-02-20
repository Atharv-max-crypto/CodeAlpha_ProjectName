import random

# List of 5 predefined words
words = ["apple", "banana", "orange", "grapes", "mango"]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Create hidden word display
display = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while incorrect_guesses < max_incorrect and "_" in display:
    print("Word:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
    
    # Check if guess is correct
    elif guess in word:
        guessed_letters.append(guess)
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!\n")
    
    # Incorrect guess
    else:
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses left:", max_incorrect - incorrect_guesses, "\n")

# Final result
if "_" not in display:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)