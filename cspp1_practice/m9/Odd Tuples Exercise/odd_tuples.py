'''#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and
returns a tuple in which contains odd index values in the input tuple
@author: gangadharsingh
'''
def odd_tuples(atup_inp):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    t_empt = ()
    j_chec = 0
    for i_chec in atup_inp:
        if j_chec % 2 == 0:
            t_empt = t_empt+ tuple(i_chec)
        j_chec += 1
    return t_empt

def main():
    '''Input : Tuple
       Output : Odd place in Tuple
    '''
    data = input()
    data = data.split()
    atup_inp=()
    for j_inp in range(len(data)):
        atup_inp += ((data[j_inp]),)
    print(odd_tuples(atup_inp))

if __name__ == "__main__":
    main()
