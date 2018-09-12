'''Найти среднее арифметическое отрицательных элементов.
Заменить минимальный элемент на это значение. '''
def num2():
    my_list = [1, -3, -6, 2, 4, 0, -5, 5, 3]
    min_arg = min(*my_list)
    average = 0
    for i in range(len(my_list)):
        if my_list[i] == min_arg:
            min_arg_num = i
        average += (lambda x: x if x < 0 else 0)(my_list[i])
    average /= len(my_list)
    my_list[min_arg_num] = average
    print(my_list)

if __name__ == "__main__":
    num2()
