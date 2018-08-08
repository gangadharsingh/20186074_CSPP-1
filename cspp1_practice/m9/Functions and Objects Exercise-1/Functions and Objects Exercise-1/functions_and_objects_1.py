'''#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList
= [1, -4, 8, -9] into [1, 4, 8, 9]
#def f(i):
#   return i+1
'''

def apply_to_each(L_inp, f_inp):
    for i_chec in range(len(L_inp)):
        L[i_chec] = f_inp(L_inp[i_chec])
    print(L_inp)

def main():
    '''Covert list into positive list
    '''
    data = input()
    data = data.split()
    list1 = []
    for j_inp in data:
        list1.append(int(j))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()
