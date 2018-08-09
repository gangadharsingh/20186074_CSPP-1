'''#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]
@author: gangadharsingh
'''
def inc(i_inp):
    '''Adding one to each elements of l_inp
    '''
    return i_inp + 1

def apply_to_each(l_inp):
    '''Adding the elements of L_inp by 1
    '''
    for i_inp in range(len(l_inp)):
        l_inp[i_inp] = inc(l_inp[i_inp])
    return l_inp

def main():
    '''Main function to increase the elements of L_inp by 1
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1))

if __name__ == "__main__":
    main()
