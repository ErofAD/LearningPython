'''Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.'''
def num6():
    my_list = []
    n = int(input())
    for i in range(n):
        new_element = int(input())
        my_list.append(new_element)
    print (my_list[0])
    for i in range(1, n):
        if my_list[i] > my_list[i-1]:
            print(my_list[i])

if __name__ == "__main__":
    num6()