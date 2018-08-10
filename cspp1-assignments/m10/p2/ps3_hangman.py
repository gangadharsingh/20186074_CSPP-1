# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i_inp in secret_word:
        if i_inp not in letters_guessed:
            return False
    return True

def getGuessedWord(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    x_inp = ""
    for i in secret_word:
        if i in letters_guessed:
            x_inp += i
        else:
            x_inp += '_'
    return x_inp

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    str_emp = ""
    str_alp = "abcdefghijklmnopqrstuvwxyz"
    for i in str_alp:
        if i not in lettersGuessed:
            str_emp += i
    return str_emp

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
str_ges = "abc"#chooseWord(loadWords())
#print("Welcome to the game, Hangman!")
print("I am thinking of a word that is", len(str_ges), "letters long")
cnt_ges = 8
print("You have", cnt_ges, "guesses left")
str_empt = ""
print(getAvailableLetters(str_empt))
for i in range(cnt_ges):
    #for i in range(len(str_ges))    
    data = input()
    if str_empt == str_ges:
        break    
    if isWordGuessed(str_ges, data):
        print("Oops! That letter is not in my word:",getGuessedWord(str_ges, data))
        str_ges += getGuessedWord(str_ges, data)
        print(getAvailableLetters(str_empt))
        cnt_ges += 1
    else:
        print("Good guess", getGuessedWord(str_ges, data))
        str_ges = getGuessedWord(str_ges, data)
        print(getAvailableLetters(str_empt))
        cnt_ges = i
    print("You have", cnt_ges, "guesses left")
    #data = input()
print("end")






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
