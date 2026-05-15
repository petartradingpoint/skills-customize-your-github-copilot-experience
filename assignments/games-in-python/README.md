
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Python Hangman game that helps students practice strings, loops, conditionals, and user input while creating an interactive console application.

## 📝 Tasks

### 🛠️ Build the main Hangman game

#### Description
Create a Hangman game that randomly selects a secret word from a predefined list and lets the player guess letters one at a time.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list of possible secret words
- Prompt the player to guess one letter per turn
- Show the current word progress using blanks and revealed letters (for example: `_ a _ g _ a _`)
- Track and display the number of incorrect guesses remaining
- Announce a win when the player guesses all letters correctly
- Announce a loss when the player runs out of guesses

### 🛠️ Add game validation and replay support

#### Description
Improve the game by validating player input and allowing the player to play again after the game ends.

#### Requirements
Completed program should:

- Reject invalid guesses such as more than one character, empty input, or non-letter characters
- Prevent duplicate guesses from counting against the player
- Ask the player whether they want to play again after each game ends
- Reset the game state correctly for a new round
