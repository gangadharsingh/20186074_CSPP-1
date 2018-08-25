'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def clean_string(string):
    '''clean string
    '''
    return re.sub('[^ a-zA-Z0-9]', '', string)
def tokenize(string):
    '''tokenizing the string
    '''
    dic_new = {}
    for i in string:
        dic_new[i] = dic_new.get(i, 0) + 1
    return dic_new

def main():
    '''tokenizw the input
    '''
    inp = int(input())
    str_new = []
    for i in range(inp):
        lis_new = input().split()
        str_new.append(lis_new)
    str_clean = []
    cnt = 0
    while cnt < len(str_new):
        for i in range(len(str_new[cnt])):
            str_clean.append(clean_string(str_new[cnt][i])+'')
        cnt += 1
    print(tokenize(str_clean))
if __name__ == '__main__':
    main()
