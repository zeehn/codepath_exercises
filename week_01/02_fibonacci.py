# This program finds the nth number in a fibonacci sequence.

def fibonacci(n):
    last, second_last, result = 1, 0, 0
    if n == 1:
        return second_last
    elif n == 2:
        return last
    else:
        for i in range(3, n + 1):
            result = second_last + last
            second_last = last
            last = result 
        return last

print(fibonacci(11))

