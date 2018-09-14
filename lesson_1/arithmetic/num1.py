'''Пользователь вводит два числа. Нужно вывести сумму, разницу и произведение этих двух чисел.
Вывести результат целочисленного деления этих двух чисел (первое на второе) и остаток от деления.'''
def num1():
    x = int(input('First number : '))
    y = int(input('Second number : '))
    print('Sum = ', x + y)
    print('Diff = ', x - y)
    print('Mult = ', x * y)
    print('Div = ', x//y)
    print('Residue = ', x % y)

if __name__ == "__main__":
    num1()