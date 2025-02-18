Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']
... 
... chosen_word = random.choice(words)
... word_display = ['_' for _ in chosen_word] 
... attempts = 8  
... 
... print("Welcome to Hangman!")
... 
... while attempts > 0 and '_' in word_display:
...     print("\n" + ' '.join(word_display))
...     guess = input("Guess a letter: ").lower()
...     
...     if guess in chosen_word:
...         for index, letter in enumerate(chosen_word):
...             if letter == guess:
...                 word_display[index] = guess  # Reveal the letter
...     else:
...         print("That letter doesn't appear in the word.")
...         attempts -= 1
... 
... if '_' not in word_display:
...     print("You guessed the word!")
...     print(' '.join(word_display))
...     print("You survived!")
... else:
...     print("You ran out of attempts. The word was: " + chosen_word)
...     print("You lost!")
