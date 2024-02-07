column_number = 1
board_arr = []
for k in range(3):
    if k == 0:
        list = []
        for i in range(17):
            if i % 4 == 2 and i > 5:
                list.append(column_number)
                column_number += 1
            else:
                list.append(" ")
        for i in list:
            count = 0
            if count == 16:
                print(i)
            else:
                print(i,end="")
                count += 1
        board_arr.append(list)

    elif k % 2 == 0:
        list = []
        for i in range(17):
            if i % 4 == 0 and i > 0:
                list.append("|")
            elif i % 4 != 0 or i == 0:
                list.append(" ")
        for i in list:
            count = 0 
            if count == 16:
                print(i)
            else:
                print(i,end="")
                count += 1
        board_arr.append(list)

    elif k % 2 == 1:
        list = []
        for i in range(17):
            if i % 4 == 0 and i > 0:
                list.append("|")
            elif i % 4 != 0 or i == 0:
                list.append(" ")
        for i in list:
            count = 0 
            if count == 16:
                print(i)
            else:
                print(i,end="")
                count += 1
        board_arr.append(list)