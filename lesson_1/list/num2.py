'''Найти среднее арифметическое отрицательных элементов.
Заменить минимальный элемент на это значение. '''
def num2():
    my_list = [1, -3, -6, 2, 4, 0, -5, 5, 3]
    min_arg = min(my_list)
    average = [0, 0]

    for i in range(len(my_list)):
        if my_list[i] == min_arg:
            min_arg_num = i
        if my_list[i] < 0:
            average[0] += my_list[i]
            average[1] += 1
        #average[0] += (lambda x: x if x < 0 else 0)(my_list[i]) #суммируем отрицательные элементы
        #average[1] += (lambda x: 1 if x < 0 else 0)(my_list[i]) #кол-во отрицательных элементов

    average[0] /= average[1]
    my_list[min_arg_num] = average[0]
    print(my_list)

if __name__ == "__main__":
    num2()
