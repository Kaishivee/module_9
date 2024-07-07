def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n < 0:
            return 'Не то'
        if n == 1:
            return 'Не то'
        elif n == 2:
            return 'Простое'
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return 'Составное'
            return 'Простое'

    return wrapper


@is_prime
def sum_three(a, b, c):
    print(a + b + c)
    return a + b + c


print(sum_three(2, 3, 6))
