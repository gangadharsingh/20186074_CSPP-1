'''Guess Number Exercise
'''
def main():
    '''
    #your code here
    '''
    inp_str = 'l'
    inp_a = 50
    inp_h = 100
    inp_l = 0
    while inp_str != 'c':
        print(inp_a)
        inp_str = input("Enter h for high,l for lower and c for correct")
        if inp_str == 'h':
            inp_h = inp_a
            inp_a = int((inp_h + inp_l)/2)
        elif inp_str == 'l':
            inp_l = inp_a
            inp_a = int((inp_h + inp_l)/2)
    print('your guess number is:', inp_a)

if __name__ == "__main__":
    main()
