def main():
    #making tictactoe
    empt_tic = empt_tictactoe()
    # print(empt_tic)
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
    if sum(i.count('x') for i in tic_tactoe) > 5 or sum(i.count('o') for i in tic_tactoe) > 5:
        return "invalid game"
    for i in range(len(tic_tactoe)):
        for j in tic_tactoe[i]:
            if j not in 'xo.':
                return "invalid input"
    return 1

def win_tictactoe(tic_tactoe):
    for i in range(len(tic_tactoe)):
        for j in range(len(tic_tactoe)):
            if sum(cnt.count(tic_tactoe[i][j]) for cnt in tic_tactoe[i]) == 3:
                return tic_tactoe[i][j]
    if sum(cnt.count(tic_tactoe[cnt][cnt]) for cnt in range(len(tic_tactoe))) == 3:
        return tic_tactoe[0][0]
    j = len(tic_tactoe)-1
    emp = ''
    while j >= 0:
        m += tic_tactoe[j][j]
        j-=1
    if m.count(m[0]) == 3:
        return m[0]
    return 'draw'
main()