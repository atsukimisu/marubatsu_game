class Player:
    def name(self):
        print('プレイヤー1の名前を入力して下さい')
        player_1 = input()
        print('プレイヤー2の名前を入力して下さい')
        player_2 = input()

    def turn(self):
        count_turn = 0
        while count_turn < 9 or winner:
            print(f"{player_1}さんのターンです")
            count_turn += 1
            if count_turn == 9 or winner:
                print(f"{player_2}さんのターンです")
                count_turn += 1