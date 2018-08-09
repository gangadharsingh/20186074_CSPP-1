'''
#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the
entry with the largest number of values associated with it. If there is more than
one such entry, return any one of the matching keys.
@author: gangadharsingh
'''

def big_gest(a_dict):
    '''
    aDict: A dictionary, where all the values are lists.
    return: The key with the largest number of values associated with it
    '''
    # Your Code Here
    max_i = 0
    cnt_i = 0
    for i_p in a_dict:
        if isinstance(a_dict[i_p], (list, tuple)):
            if len(a_dict[i_p]) > max_i:
                max_i = len(a_dict[i_p])
                cnt_i = i_p
        if max_i == 0 and cnt_i == 0:
            max_i = 1
            cnt_i = i_p
    return cnt_i
def main():
    '''s=input()
    l=s.split()
    if l[0][0] not in aDict:
        aDict[l[0][0]]=[l[1]]
    else:
        aDict[l[0][0]].append(l[1])'''
    a_dict = {1 : [1, 2, 3], 2 : (1, 2, 3), 4 : '5', 5 : 5}
    print(big_gest(a_dict))

if __name__ == "__main__":
    main()
