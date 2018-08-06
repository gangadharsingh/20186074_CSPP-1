'''
# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.
# This function takes in one number and returns one number.
@author: gangadharsingh
'''

def square(x_inp):
    '''
    x: int or float.
    '''
    # Your code here
    return x_inp**2
    # Correct

def main():
    '''
    input int value
    '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
