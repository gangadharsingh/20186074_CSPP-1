# Assignment-3
'''
At this point, we have written code to generate a random hand and display that
hand to the user. We can also ask the user for a word (Python's input) and score
the word (using your getWordScore). However, at this point we have not written any
code to verify that a word given by a player obeys the rules of the game. A valid
word is in the word list; and it is composed entirely of letters from the current
hand. Implement the isValidWord function.
Testing: Make sure the test_isValidWord tests pass. In addition, you will want to
test your implementation by calling it multiple times on the same hand - what should
the correct behavior be? Additionally, the empty string ('') is not a valid word - if
you code this function correctly, you shouldn't need an additional check for this condition.
Fill in the code for isValidWord in ps4a.py and be sure you've passed the appropriate
tests in test_ps4a.py before pasting your function definition here.
@author: gangadharsingh
'''

def is_validword(word, hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    cnt = 0
    if word in word_list:
        for i_inp in word:
            if i_inp in hand and hand[i_inp] != 0:
                cnt += 1
    return cnt == len(word)

def main():
    '''Main function
    '''
    word = input()
    n_inp = int(input())
    adict = {}
    for data in range(n_inp):
        data = input()
        l_inp = data.split()
        adict[l_inp[0]] = int(l_inp[1])
    l2_inp = input().split()
    print(is_validword(word, adict, l2_inp))

if __name__ == "__main__":
    main()
