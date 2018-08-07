# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumof_digits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n >= 1:
    	return n%10 + sumof_digits(n//10)
    return n 


def main():
    a = input()
    print(sumof_digits(int(a)))  

if __name__ == "__main__":
    main()

