'''Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях числа 2, и т.д.'''

def num8(n):
    my_list = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(abs(i-j))
        my_list.append(row)
    for i in range(n):
        print(my_list[i])

if __name__ == "__main__":
    num8(4)
