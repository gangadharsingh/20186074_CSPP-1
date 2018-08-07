'''
# Exercise: Is In
# Write a Python function, isIn(char, aStr), that
takes in two arguments a character and String and returns the isIn(char, aStr)
which retuns a boolean value.
# This function takes in two arguments character and String and returns one boolean value.
@author: gangadharsingh
'''
def is_in(char_inp, astr_inp):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if char_inp == astr_inp[0]:
        return True
    elif len(astr_inp) == 1:
        return False
    else:
        return is_in(char_inp, astr_inp[1:])

def main():
    '''input : letter, string
        output: True if found or False when not found
    '''
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))

if __name__ == "__main__":
    main()
