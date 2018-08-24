'''checking validation and then who wins the game
'''
def main():
    '''tic tac toe game
    '''
    #making tictactoe
    empt_tic = empt_tictactoe()
    #checking input is valid or not
    if inp_validation(empt_tic) == 1:
        print(win_tictactoe(empt_tic))
    else:
        chec = inp_validation(empt_tic)
        if chec == 1:
            print('invalid game')
        elif chec == 2:
            print('draw')
        elif chec == 3:
            print('x')
        elif chec == 4:
            print('o')
        elif chec == 5:
            print(empt_tic[0][0])
        elif chec == 6:
            print(empt_tic[0][2])

def empt_tictactoe():
    '''creating empty tic tac toe
    '''
    tic_tactoe = []
    for _ in range(3):
        list_temp = input().split()
        tic_tactoe.append(list_temp)
    return tic_tactoe
    #either x or y count should not be greater than 5

def inp_validation(tic_tactoe):
    '''checking whether tic tac toe is valid or not
    '''
    if sum(i.count('x') for i in tic_tactoe) > 5 or sum(i.count('o') for i in tic_tactoe) > 5:
        return "invalid game"
    for _, row  in enumerate(tic_tactoe):
        for col in row:
            if col not in 'xo.':
                return "invalid input"
    return 1

def win_tictactoe(tic_tactoe):
    '''checking wining team
    '''
    c_x = sum([i.count('x') for i in tic_tactoe])
    c_o = sum([i.count('o') for i in tic_tactoe])
    if c_x == 3 and c_o == 3:
        return 1#'invalid game'
    if c_x+c_o == 9:
        return 2#'draw'
    if c_x == 3:
        return 3#'x'
    if c_o == 3:
        return 4#'o'
    if tic_tactoe[0][0] == tic_tactoe[1][1] == tic_tactoe[2][2]:
        return 5#'tic_tactoe[0][0]'
    if tic_tactoe[0][2] == tic_tactoe[1][1] == tic_tactoe[2][0]:
        return 6#'tic_tactoe[0][2]'
main()
