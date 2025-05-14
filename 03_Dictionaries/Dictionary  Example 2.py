theboard = { 'Top-L' : ' ', 'Top-M' : ' ', 'Top-R' : ' ', 'Mid-L' : ' ', 'Mid-M' : ' ', 'Mid-R' : ' ', 'Low-L' : ' ', 'Low-M' : ' ', 'Low-R' : ' ' }
def printboard(board):
    print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
    print('--+--+--')
    print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
    print('--+--+--')
    print(board['Low-L'] + '|' + board['Low-M'] + '|' + board['Low-R'])
turn = "X"
for i in range(9):
    printboard(theboard)
    print('Turn for ' + turn + '. Move on which space...?')
    move = input()
    theboard[move] = turn
    if turn == 'X':
        turn = "0"
    else:
        turn = "X"
print(theboard)