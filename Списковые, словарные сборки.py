num = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def func(x):
    return x % 2


def func2(x):
    return x * x


step1 = filter(func, num)
step_2 = map(func2, step1)

print(list(step_2))
