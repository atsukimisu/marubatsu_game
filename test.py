class Unko:

    def input_name(self):
        print("名前を入力して下さい")
        name = input()
        return name
    
a = Unko
print(a.input_name())