def next_prime(num):
    if num < 2:
        return 2
    n = 2
    while True:
        i, flag = 2, False
        while i < n:
            if n % i == 0:
                flag = True
                break
            i += 1
        if flag == False and n > num and i == n:
            return n
        n += 1

print(next_prime(3))
print(next_prime(17))
print(next_prime(55))
print(next_prime(-10))
