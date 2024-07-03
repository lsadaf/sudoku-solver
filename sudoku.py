from typing import Optional, List


def solver(board: list[list]) -> Optional[list[list]]:
    size = len(board)
    #print(board)
    empty_i, empty_j = 10, 10
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                empty_i, empty_j = i, j
                break
        if empty_i != 10 and empty_j != 10:
            break
    if empty_i == 10 and empty_j == 10:
        return board

    #print(empty_i,empty_j)
    # backtrack
    for num in range(size):
        number = num+1
        #print(number)
        if number in board[empty_i]:
            #print("number exists in row")
            continue
        flag = False
        for j in range(size):
            if board[j][empty_j] == number:
                #print("number exists in col")
                flag = True
                break
        if flag:
            continue

        board[empty_i][empty_j] = number
        if solver(board) is not None:
            return board
        else:
            board[empty_i][empty_j] = 0

    return
