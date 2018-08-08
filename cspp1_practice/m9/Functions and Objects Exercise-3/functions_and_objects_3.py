'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]
@author: ganagdharsingh
'''
def square(i_inp):
    '''Squaring the elements
    '''
    return i_inp ** 2

def apply_to_each(L_inp, f):
    '''Function calling the square function
    '''
    for i_inp in range(len(L_inp)):
        L_inp[i_inp] = f(L_inp[i_inp])
    return L_inp

def main():
    '''Squaring each elements of given list
    '''
    data = input()
    data = data.split(" ")
    list1 = []
    for j_inp in data:
        list1.append(int(j_inp))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()