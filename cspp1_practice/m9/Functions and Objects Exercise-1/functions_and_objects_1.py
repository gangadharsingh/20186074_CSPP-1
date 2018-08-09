'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]
@author: ganagadharsingh
'''

def apply_to_each(l_inp, f_inp):
    '''converting the negative value in positive
    '''
    for i_inp in range(len(l_inp)):
        if l_inp[i_inp] < 0:
            l_inp[i_inp] = f_inp(l_inp[i_inp])
    return l_inp

def main():
    ''' List of negative and positive number.
        Output: List of positive number
    '''
    data = input()
    data = data.split()
    list1 = []
    for j_inp in data:
        list1.append(int(j_inp))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
