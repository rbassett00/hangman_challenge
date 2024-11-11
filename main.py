import random
import linecache

# this function uses the random and linecache libraries to randomly choose a line from words.txt
# linecache makes it very easy to store a line
def get_word():
    random_num = random.randint(1, 10)
    line = linecache.getline("words.txt", random_num)
    return line

# updates the display by checking where the letter is in the word by comparing the indices after enumerating the word
def update_display(display, word, user_input):
    new_display = list(display)
    for index, letter in enumerate(word):
        if user_input.lower() == letter:
            new_display[index] = letter
    return "".join(new_display)

# checks win condition by seeing if there are anymore '_' in the display, if not, the word has been fully guessed
def check_win(display):
    if "_" in display:
        return False
    else:
        return True

# storing all the states in a list makes them easier to get and store
hangman_states = [
    """
       |----|
       |    |
       |    
       |   
       |    
       |   
     -----
    """,
    """
       |----|
       |    |
       |    0
       |   
       |    
       |   
     -----
    """,
    """
       |----|
       |    |
       |    0
       |    |
       |    
       |   
     -----
    """,
    """
       |----|
       |    |
       |    0
       |   /|
       |    
       |   
     -----
    """,
    """
       |----|
       |    |
       |    0
       |   /|\\
       |    
       |   
     -----
    """,
    """
       ------
       |    |
       |    0
       |   /|\\
       |   / 
       |   
     -----
    """,
    """
       ------
       |    |
       |    0
       |   /|\\
       |   / \\
       |   
     -----
    """
]

hangman = """                                                 
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███ ██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""
print(hangman)
print("Welcome to the game! Press 0 to quit")

# this while loop allows the player to play again after they finish
while True:
    word = get_word()
    word_length = len(word)-1
    display = "_" * word_length
    state = 0
    already_guessed = []

    print(f"Your word is {word_length} letters long")
    print(hangman_states[state])
    print(display)

    # this while loop allows the player to guess over and over
    while True:
        user_input = input("Guess a letter: ")
        if user_input == "0":  # exit check first then leave
            break
        if not user_input.isalpha() or len(user_input) > 1:  # checks if input is a single letter (no #s/weird chars)
            print("Input must be one letter")
        elif user_input in already_guessed:  # inform the player if it's already guessed, does not count it as a mistake
            print("Letter already guessed!")
        elif user_input.lower() in word:  # .lower() means capital letters will be fine, the player won't get penalized
            display = update_display(display, word, user_input)
            print(display)
            if check_win(display) is True:  # check for win after updating display
                print("You Win!")
                break  # leave the loop so the player can get a new word
            already_guessed.append(user_input)
        else:  # updated the hangman state and inform the player they lost if they reach the final state
            print(f"{user_input} is not in the word")
            state += 1
            print(hangman_states[state])
            print(display)
            if state == 6:
                print(f"You murderer...your word was '{word}'")
                break
            already_guessed.append(user_input)
    if user_input == "0":  # exits if the player wants to leave during the game
        break
    user_input = input("Do you wish to play again?(y/n): ")  # asks player if they want to play again
    if user_input.lower() == "n" or user_input == "0":  # n or 0 exits the program
        break



