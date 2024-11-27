# プレイヤー１の名前を入力
# プレイヤー２の名前を入力

# 現在の盤面を表示
# 「{プレイヤー１}の番です」と表示
# 勝敗とターン数を判定
# 現在の盤面を表示
# 「{プレイヤー２}の番です」と表示
# 勝敗をターン数を判定

# 「{プレイヤー1or2さんの勝利です}」と表示する
column_index = [6, 10, 14]
row_index = [2, 4, 6]
row = 0
column = 0
count = 0

column_number = 1
board_arr = []
for k in range(8):
    if k == 0:
        values = []
        for i in range(17):
            if i % 4 == 2 and i > 5:
                values.append(str(column_number))
                column_number += 1
            else:
                values.append(" ")
        board_arr.append(values)

    elif k % 2 == 0:
        values = []
        for i in range(17):
            if i % 4 == 0 and i > 0:
                values.append("|")
            elif i == 0:
                row = int(k/2)
                values.append(str(row))
            elif i % 4 != 0 or i == 0:
                values.append(" ")
        board_arr.append(values)

    elif k % 2 == 1:
        values = []
        for i in range(17):
            if i % 4 == 0 and i > 0:
                values.append("+")
            elif i % 4 != 0 and i > 3:
                values.append("-")
            elif i % 4 != 0 or i == 0:
                values.append(" ")
        board_arr.append(values)

class Player:
    def __init__(self, name, win, turn, mark) -> None:
        self.name = name
        self.win = win
        self.turn = turn
        self.mark = mark

    def your_turn(self):
        print(f'{self.name}さんのターンです')
        print('行と列を選んでください：', end="")
        # row = int(input())
        # print('列を選んでください：', end="")
        # column = int(input())


class GameLogic:
    def weather_to_win(board_arr, player: Player):
        player.turn += 1
        # 縦列の評価
        for i in column_index:
            if board_arr[row_index[0]][i] == board_arr[row_index[1]][i] == board_arr[row_index[2]][i] != " ":
                player.win = True

        # 横列の評価
        for i in row_index:
            if board_arr[i][column_index[0]] == board_arr[i][column_index[1]] == board_arr[i][column_index[2]] != " ":
                player.win = True

        # 斜めの評価
        if board_arr[row_index[0]][column_index[0]] == board_arr[row_index[1]][column_index[1]] == board_arr[row_index[2]][column_index[2]] != " ":
            player.win = True
        elif board_arr[row_index[0]][column_index[2]] == board_arr[row_index[1]][column_index[1]] == board_arr[row_index[2]][column_index[0]] != " ":
            player.win = True

    def winner(player: Player):
        print(f'{player.name}さんの勝利です！') 



class GameBoard:
    def show_board():
        for i in board_arr:
            for j in range(17):
                if j == 16:
                    print(i[j])
                else:
                    print(i[j], end="")

    def fill_board(row: int, column: int, player: Player):
        board_arr[2 * row][4 * column + 2] = player.mark



def main():
    # 表示する名前を入力
    print('プレイヤー1の名前を入力して下さい')
    player_1 = Player(name=input(), win=False, turn=0, mark="￮")
    print('プレイヤー2の名前を入力して下さい')
    player_2 = Player(name=input(), win=False, turn=0, mark="×")
    GameBoard.show_board()

    while player_1.win == False and player_2.win == False:
        # プレイヤー１が入力する場所を入力
        player_1.your_turn()

        row, column = input().split()
        # if row not in ["1", "2", "3"]:
        #     print("invalid input")
        #     continue
        # if column not in ["1", "2", "3"]:
        #     print("invalid input")
        #     continue
        try:
            row = int(row)
            column = int(column)
        except ValueError as value_error:
            print("value_error: %s", value_error)
            continue

        # if board_arr[row][column] != " " or isinstance(row, float) or isinstance(column, float):
        #     print("もう一度入力して下さい")

        # プレイヤー１が盤面を埋めて、表示
        GameBoard.fill_board(row, column, player_1)
        GameBoard.show_board()
        GameLogic.weather_to_win(board_arr, player_1)
        if player_1.win == True:
            GameLogic.winner(player_1)
            break
        elif player_1.win == False and player_1.turn == 5:
            print('引き分けです…')
            break

        # プレイヤー２が入力する場所を入力
        player_2.your_turn()
        row, column = map(int, input().split())

        # プレイヤー２が盤面を埋めて、表示
        GameBoard.fill_board(row, column, player_2)
        GameBoard.show_board()
        GameLogic.weather_to_win(board_arr, player_2)
        if player_2.win == True:
            GameLogic.winner(player_2)
            break

if __name__ == '__main__':
    main()
