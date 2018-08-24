def main():
    #making tictactoe
    empt_tic = empt_tictactoe()
    print(empt_tic)
    #checking input is valid or not
    if inp_validation(empt_tic) == 1:
        print(win_tictactoe(empt_tic))
    else:
        print(inp_validation(empt_tic))

def empt_tictactoe():
    '''
    '''
    row = []
    for i in range(3):
        list_temp = input().split()
        row.append(list_temp)
    return row
    #either x or y count should not be greater than 5

def inp_validation(tic_tactoe):
    if tic_tactoe.count('x') > 5 or tic_tactoe.count('o') > 5:
        return "invalid game"
    for i in range(len(tic_tactoe)):
        for j in tic_tactoe[i]:
            if j not in 'xo.':
                return "invalid input"
    return 1

def win_tictactoe(tic_tactoe):
    return True


main()