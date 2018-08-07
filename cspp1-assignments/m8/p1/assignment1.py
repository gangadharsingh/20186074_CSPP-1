'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
and returns the factorial of given number.
# This function takes in one number and returns one number.
@author: gangadharsingh
'''

def fact_rial(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n == 1:
    	return 1
    return fact_rial(n-1) * n
    


def main():
    a = input()
    print(fact_rial(int(a)))    

if __name__== "__main__":
    main()
