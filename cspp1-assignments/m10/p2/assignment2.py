'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list

def choose_word(word_list):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
word_list = loadWords()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in letters_guessed:
        if i in secret_word:
            return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    var_temp_string = ""
    for var_iteratble in secret_word:
        if var_iteratble not in letters_guessed:
            var_temp_string += "_"
        else:
            var_temp_string += var_iteratble
    return var_temp_string

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str2 = ""
    chk_str = string.ascii_lowercase
    for i in chk_str:
        if i not in letters_guessed:
            str2 += i
    return str2

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    wrong_cnt = 8
    emp_user = ""
    empt_tem = ""
    print(secretWord)
    while True:
        print("-----------")
        print("You have " +  str(wrong_cnt) +" guesses left.")
        print("Available letters: " + get_available_letters(emp_user.split()))
        char_entered = input("Please guess a letter: ")
        emp_user = emp_user + " " + char_entered
        if char_entered in empt_tem:
            print("Oops! You've already guessed that letter:" + \
                get_guessed_word(secretWord, emp_user.split()))
        else:
            if is_word_guessed(secretWord, char_entered.split()):
                print("Good guess: " + get_guessed_word(secretWord, emp_user.split()))
            else:
                print("Oops! That letter is not in my word: " + \
                    get_guessed_word(secretWord, emp_user.split()))
                wrong_cnt -= 1
        if get_guessed_word(secretWord, emp_user.split()) in secretWord:
            print("Congratulations, you won!")
            break
        elif wrong_cnt == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break
        empt_tem += emp_user

def main():
    '''
    Main function for the given program
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = choose_word(word_list).lower()
    hangman(secretWord)
if __name__ == "__main__":
    main()
