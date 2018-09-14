'''Необходимо решить квадратное уравнение ax2 + bx + c = 0.
Коэффициенты a, b, c вводит пользователь.'''
def num3():
    print('ax2 + bx + c = 0')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    print('%i * x2 + %i * x + %i = 0' % (a, b, c))
    d = b**2 - 4*a*c
    if d < 0:
        print('Корней нет')
    elif d == 0:
        print('Уравнение имеет один корень:')
        x = -b/(2*a)
        print('x = ', x)
    else:
        print('Уравнение имеет два корня:')
        x1 = (-b + d ** 0.5)/(2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print('x1 = %i , x2 = %i' % (x1, x2))

if __name__=="__main__":
    num3()
