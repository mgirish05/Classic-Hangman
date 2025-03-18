import random

words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word] 
attempts = 8
guessed_letters = set()

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    
    guessed_letters.add(guess)
    
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Reveal the letter
    else:
        print("That letter doesn't appear in the word.")
        attempts -= 1

if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")
