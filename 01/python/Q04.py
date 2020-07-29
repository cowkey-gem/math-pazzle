# プログラマ脳を鍛える数学パズル Q04

import sys

stack = [int(sys.argv[1])]
workers = int(sys.argv[2])

def split(bar):
    split_bar = [bar // 2, bar // 2]
    if bar % 2 != 0:
        split_bar[0] += 1

    return [ x for x in split_bar if x > 1]

def turn():
    global stack, workers
    bars = []
    for worker in range(workers):
        bar = stack.pop()
        stack_size = len(stack)
        bars += split(bar)
        
        if len(stack) == 0:
            break
    stack = bars + stack

i = 0
while len(stack) > 0:
    print(stack)
    i += 1
    turn()

print(i)


