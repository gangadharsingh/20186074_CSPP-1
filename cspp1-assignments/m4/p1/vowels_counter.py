'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
'''

def main():
    s_inp = input()
    '''
    # the input string is in s_inp
    # remove pass and start your code here
    '''
    vowel_str="aeiou"
    cnt_strt=0
    for i in s_inp:
        if i == vowel_str:
            cnt_strt += 1
    print(cnt_strt)

if __name__== "__main__":
    main()
