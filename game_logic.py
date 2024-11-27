from player import Player

column_index = list(range(6,15,4))
row_index = list(range(2,7,2))

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

class GameLogic:
        def __init__(self, player: Player):
                self.player = player

        def weather_to_win(self, arr_board, player: Player):
            # 縦列の評価
            for i in column_index:
                if arr_board[row_index[0]][i] == arr_board[row_index[1]][i] == arr_board[row_index[2]][i] != " ":
                    player.win = True

            # 横列の評価
            for i in row_index:
                if arr_board[i][column_index[0]] == arr_board[i][column_index[1]] == arr_board[i][column_index[2]] != " ":
                    player.win = True

            # 斜めの評価
            if arr_board[row_index[0]][column_index[0]] == arr_board[row_index[1]][column_index[1]] == arr_board[row_index[2]][column_index[2]] != " ":
                player.win = True
            elif arr_board[row_index[0]][column_index[2]] == arr_board[row_index[1]][column_index[1]] == arr_board[row_index[2]][column_index[0]] != " ":
                player.win = True

        def winner(self, player: Player):
             if player.win == True:
                  print(f'{player.name}さんの勝利です')
