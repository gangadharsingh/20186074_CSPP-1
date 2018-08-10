'''
#Exercise: Integer Division Exercise
#Modify the code for integer_division so that this error does not occur.
@author: gangadharsingh
'''
def integer_division(x_inp, a_inp):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x_inp > a_inp:
        count += 1
        x_inp = x_inp - a_inp
    return count

def main():
    '''Input :positive number
       Output:x divided by a
    '''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
