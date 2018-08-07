'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
and returns the factorial of given number.
# This function takes in one number and returns one number.
@author: gangadharsingh
'''

def fact_rial(n_inp):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_inp == 0:
        return 1
    elif n_inp == 1:
        return 1
    return fact_rial(n_inp-1) * n_inp

def main():
    '''print factorial
    '''
    a_inp = input()
    print(fact_rial(int(a_inp)))

if __name__ == "__main__":
    main()
