'''Получить список из положительных элементов другого списка,
стоящих на четных местах [1, -3, -6, 2, 4, 0, -5, 5, 3]'''
def num4():
    my_list = [1, -3, -6, 2, 4, 0, -5, 5, 3]
    new_list = []
    for i in range(len(my_list)):
        if (i % 2 == 0) and (my_list[i] > 0):
            new_list.append(my_list[i])
    print(new_list)

if __name__ == "__main__":
    num4()
