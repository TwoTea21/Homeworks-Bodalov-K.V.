import math


def divide(first, second):
    if second != 0:
        result = first / second
        print('Ответ равен:', result)
    else:
        print('Ответ равен:', math.inf)
