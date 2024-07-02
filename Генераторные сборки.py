def oper(operation):  # Задача 1:
    if operation == 'div':
        def div(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                print('Нельзя делить на ноль')

        return div

    elif operation == 'mult':
        def mult(x, y):
            return x * y

        return mult


my_func = oper('div')
print(my_func(3, 0))

my_func = oper('mult')
print(my_func(3, 3))

square = lambda x: (x ** 2)  # Задача 2
print(square(3))


def square_def(x):
    return x ** 2


print(square_def(4))


class Rect:  # Задача 3:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f'Сторона а: {self.a}')
        print(f'Сторона b: {self.b}')

    def __call__(self):
        return f'Площадь равна: {self.a * self.b}'


my_square = Rect(3, 4)
print(my_square())
