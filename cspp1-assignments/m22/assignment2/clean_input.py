'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    str_add = ''
    for i in string:
    	if i in ['^a-Z']:
    		str_add += i
    return str_add
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
