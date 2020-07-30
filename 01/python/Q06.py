# プログラマ脳を鍛える数学パズル Q06

count = 0
for n in [i for i in range(2, 10001, 2)]:
    i = n * 3 + 1
    arr = []
    while True:
        arr.append(i)
        if i % 2 == 0:
            i = i // 2
        else :
            i = i * 3 + 1

        if i == n:
            count += 1
            break
        if i in arr:
            break;
print(count)

# true/falseを返すような関数として切り出すのもありか
