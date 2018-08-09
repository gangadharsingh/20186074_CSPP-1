'''
#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number
of values associated with a dictionary.
'''
def how_many(a_dict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    list_in = []
    for i_in in a_dict.values():
        if isinstance(i_in, list):
            list_in.extend(i_in)
        elif isinstance(i_in, tuple):
            list_in.extend(list(i_in))
        elif isinstance(i_in, (int, float)):
            list_in.append(i_in)
        else:
            list_in.append(0.0)
    return sum(list_in)

def main():
    '''s=input()
    l=s.split()
    if l[0][0] not in aDict:
        aDict[l[0][0]]=[l[1]]
    else:
        aDict[l[0][0]].append(l[1])'''
    a_dict = {1:[1, 2, 3], 2:(1, 2, 3), 4:'5', 5:5}
    print(how_many(a_dict))

if __name__ == "__main__":
    main()
