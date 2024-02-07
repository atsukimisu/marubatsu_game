class GameBoard:
    def current_board(self):
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

        for i in board_arr:
            for j in range(17):
                if j == 16:
                    print(i[j])
                else:
                    print(i[j], end="")
    
    def attack(self):
        print("行を選んでください")
        column_index = int(input())
        print("列を選んでください")
        row_index = int(input())
        
