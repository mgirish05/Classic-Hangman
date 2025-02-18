# Classic-Hangman
A simple command-line Hangman game implemented in Python.

Features
- Randomly selects a word from a predefined list.
- Allows the player to guess letters until the word is fully revealed or attempts run out.
- Provides feedback on correct and incorrect guesses.
- Displays the word with guessed letters revealed and underscores for remaining letters.

Technologies Used
- Python 3
- Random module for word selection

## How to Run
1. Ensure you have Python installed on your system.
2. Download or clone this repository.
3. Open a terminal or command prompt and navigate to the project folder.
4. Run the script using:
   bash
   python hangman.py
   
5. Follow the on-screen prompts to play the game.

Usage
- The game starts by displaying a hidden word represented by underscores.
- The player inputs a letter guess.
- If the letter is in the word, it is revealed in the correct positions.
- If the letter is incorrect, an attempt is deducted.
- The game ends when the player correctly guesses the word or runs out of attempts.

Example Run

Welcome to Hangman!
_ _ _ _ _ _
Guess a letter: o
_ _ _ h o _
Guess a letter: n
That letter doesn't appear in the word.
Remaining attempts: 7
...


Future Enhancements
- Add difficulty levels with different word lists.
- Implement word definitions as hints.
- Store a high-score system to track best players.
