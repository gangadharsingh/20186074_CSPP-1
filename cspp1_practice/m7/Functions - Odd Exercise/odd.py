'''
# Exercise: odd
# Write a Python function, odd, that takes in one
number and returns True when the number is odd and False otherwise.
# You should use the % (mod) operator, not if.
# This function takes in one number and returns a boolean.
@author: gangadharsingh
'''

def odd(x_inp):
    '''
    x: int or float.
    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x_inp % 2 != 0
def main():
    '''give output True if number is odd or False if number is even
    '''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
