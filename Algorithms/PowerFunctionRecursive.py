def power(val, num):
    if num == 0:
        print("returning 1")
        return 1
    elif num % 2 == 0:
        temp = power(val, num//2)
        return temp * temp
    elif num < 0:
        return 1/power(val, -num)
    elif num % 2 != 0:
        return val * power(val, num-1)


print(power(10, 4))
print(power(3, 3))
print(power(3, -3))
print(power(2, 0))

