'''Дан список [1, 4, 3, 8, 10]. Необходимо вернуть: список квадратов чисел, список квадратов четных элементов на нечетных позициях.'''
def num7():
    my_list = [1, 4, 3, 8, 10]
    sqr_list = [x*x for x in my_list]
    print(sqr_list)
    new_list = []
    for i in range(len(my_list)):
        if (i % 2 == 1) and (my_list[i] % 2 == 0):
            new_list.append(my_list[i]**2)
    print(new_list)

if __name__ == "__main__":
    num7()