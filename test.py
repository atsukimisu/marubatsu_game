a = list(range(6,15,4))
b = list(range(2,7,2))
from player import Player
# print(a)
# print(b)

# # 縦列の評価
# for i in a:
#     if arr_board[b[0]][i] == arr_board[b[1]][i] == arr_board[b[2]][i] != " ":
#         player_1.winner = True
    
# # 横列の評価
# for i in b:
#     if arr_board[i][a[0]] == arr_board[i][a[1]] == arr_board[i][a[2]] != " ":
#         player_1.winner = True

# # 斜めの評価
# if arr_board[b[0]][a[0]] == arr_board[b[1]][a[1]] == arr_board[b[2]][a[2]] != " ":
#     player_1.winner = True
# elif arr_board[b[0]][a[2]] == arr_board[b[1]][a[1]] == arr_board[b[2]][a[0]] != " ":
#     player_1.winner = True

# class Example:
#     def __init__(self, name, win: bool, turn:bool):
#         self.name = name
#         self.win = False
#         self.turn = False

    
column_number = 1
board_arr = []
for k in range(8):
    if k == 0:
        list = []
        for i in range(17):
            if i % 4 == 2 and i > 5:
                list.append(str(column_number))
                column_number += 1
            else:
                list.append(" ")
        board_arr.append(list)

    elif k % 2 == 0:
        list = []
        for i in range(17):
            if i % 4 == 0 and i > 0:
                list.append("|")
            elif i == 0:
                row = int(k/2)
                list.append(str(row))
            elif i % 4 != 0 or i == 0:
                list.append(" ")
        board_arr.append(list)

    elif k % 2 == 1:
        list = []
        for i in range(17):
            if i % 4 == 0 and i > 0:
                list.append("+")
            elif i % 4 != 0 and i > 3:
                list.append("-")
            elif i % 4 != 0 or i == 0:
                list.append(" ")
        board_arr.append(list)

# class Board:
#     def show_board():
#         for i in board_arr:
#             for j in range(17):
#                 if j == 16:
#                     print(i[j])
#                 else:
#                     print(i[j], end="")

# def fill_board(row: int, column: int):
#     board_arr[2 * row][4 * column + 2] = '⚪︎'

# fill_board(1, 2)
# for i in board_arr:
#             for j in range(17):
#                 if j == 16:
#                     print(i[j])
#                 else:
#                     print(i[j], end="")

class Do:
    def __init__(self, row, column, player: Player):
        self.row = row
        self.column = column
        self.player = player

    def fill(self, player):
        print('アババババ')
        self.row = int(input())
        print('オロロロロ')
        self.column = int(input())
        board_arr[self.row * 2][self.column * 4 + 2] = player.mark

player_3 = Player(name=input(),  )
        

