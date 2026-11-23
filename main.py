jadval = """ --- --- ---
| 1 | 2 | 3 |
 --- --- ---
| 4 | 5 | 6 |
 --- --- ---
| 7 | 8 | 9 |
 --- --- ---
"""

wins = ["123", "147", "159", "753", "789", "456", "369", "258"]

x_inputs = ""
o_inputs = ""

winners = False

for i in range(1, 10):
    if winners:
        break
    if i % 2 == 1:
        x_input = input(jadval + "X o'yinchi katak tanlasin: ")
        while x_input in x_inputs + o_inputs or x_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            x_input = input("X o'yinchi qayta katak tanlasin: ")
        x_inputs = x_inputs + x_input
        jadval = jadval.replace(x_input, "X")
        for win in wins:
            if win[0] in x_inputs and win[1] in x_inputs and win[2] in x_inputs:
                print(jadval + "X o'yinchi g'olib boldi !!!")
                winners = True
    elif i % 2 == 0:
        o_input = input(jadval + "O o'yinchi katak tanlasin: ")
        while o_input in o_inputs + x_inputs or o_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            o_input = input("O o'yinchi qayta katak tanlasin: ")
        o_inputs = o_inputs + o_input
        jadval = jadval.replace(o_input, "O")
        for win in wins:
            if win[0] in o_inputs and win[1] in o_inputs and win[2] in o_inputs:
                print(jadval + "O o'yinchi g'olib boldi !!!")
                winners = True
else:
    if not winners:
        print(jadval + "Durrang !!!")