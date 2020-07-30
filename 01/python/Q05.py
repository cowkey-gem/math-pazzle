# プログラマ脳を鍛える数学パズル Q05

def counter(yen, count, list):
    if count == 0 or yen < 0 or len(list) == 0:
        return 0
    if yen == 0:
        return 1
    sum = 0
    for i in range(len(list)):
        sum += counter(yen - list[i], count - 1, list[i::])
    return sum

print(counter(1000, 3, [500, 100, 50, 10]))

