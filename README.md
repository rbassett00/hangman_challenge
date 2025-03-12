# Hangman 
Hangman challenge for BYU student programer position, this took me about 2 hours to complete 

## Description
* The program conists of 2 main while loops and some helper functions, and a word.txt file
* word.txt - I used a file for the words to make it easier to add to in the future
* First loop - Allows the player to play again as amny times as they'd like
* Second loop - the actual game loop, looping through the user's inputs as they guess letters
* check_win function - checks to see if the player won after every correct guess
* get_word function - gets the word from word.txt, using a random number to pick a randome line (word) from the file
* update_display - enumerates the word and display to place the letter in the correct place

## Key features
* The game will end when you get to the final hangman stage, but will allow you to play again
* It keeps track of letters you've already guessed, and won't penalize you (progress the hangman stage) if you guess it again
* You can quit anytime with 0

  Please look at my main.py for comments about my thought process!
