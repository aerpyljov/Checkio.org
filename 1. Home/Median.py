def checkio(numbers):
    numbers.sort()
    len_num = len(numbers)
    if len_num == 1:
        return numbers[0]
    elif len_num % 2 != 0:
        return numbers[int(len_num / 2)]
    else:
        return (numbers[int(len_num / 2)] + numbers[int((len_num / 2) - 1)]) / 2.0





print(checkio([1, 2, 3, 4, 5]))

print(checkio([3, 1, 2, 5, 3]))

print(checkio([1, 300, 2, 200, 1]))

print(checkio([3, 6, 20, 99, 10, 15]))

