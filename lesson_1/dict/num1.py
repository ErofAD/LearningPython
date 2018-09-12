'''Есть данные с компьютерной игры:
69485 Jack
95715 Michail
95715 Alex
83647 Morgan
197128 Jerry
95715 Nikole
93289 Lauren
где можно найти очки, которые заработал пользователь.
Нужно создать словарь из этих данных, найти победителя.'''
def num1():
    dict = {'Jack': 69485,
            'Michail': 95715,
            'Alex': 95715,
            'Morgan': 83647,
            'Jerry': 197128,
            'Nicole': 95715,
            'Lauren': 93289}
    maximum = 0
    for key, value in dict.items():
        if value > maximum:
            winner = key
            maximum = value

    print("Winner: %s, Score: %s" % (winner, maximum))

if __name__ == "__main__":
    num1()
