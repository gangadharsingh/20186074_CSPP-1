'''
Replace all the special characters(!, @, #, $, %, ^, &, *)
in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with
these special characters

'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_inp = 'abc@#'#input()
    str_emt = ""
    str_cmp = "!@#$%^&*"
    i = len(str_inp)
    j = 0
    m = 0
    for i in str_inp:
        if i in str_cmp:
            str_emt += " "
        else:
            str_emt += i
    print(str_emt)


if __name__ == "__main__":
    main()
