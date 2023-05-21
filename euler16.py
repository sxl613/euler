import matplotlib.pyplot as plt
def sum_digits(n):
    res = 0
    while n > 0:
        res += n%10
        n = n//10
    return res


print(sum_digits(2**1000))