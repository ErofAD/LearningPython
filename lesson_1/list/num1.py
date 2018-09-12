'''Вводятся 10 целых чисел от пользователя.
Необходимо четные добавлять в начало списка,
 а нечетные - в конец.'''

def num1 ():
    my_list = []
    for i in range(10):
        x = int(input("Введите число: "))
        if x%2==0:
            my_list.insert(0, x)
        else:
            my_list.append(x)
    print('My list ', my_list)

if __name__=="__main__":
    num1()