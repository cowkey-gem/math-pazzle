# プログラマ脳を鍛える数学パズル Q03
cards = [False for i in range(0, 100)]
for i in range(1, 100):
    for j in range(i, 101, i + 1):
        cards[j] = not cards[j] 
for i in [i + 1 for i in range(len(cards)) if not cards[i]]:
    print(i)
