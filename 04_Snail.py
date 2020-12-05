from itertools import chain
def snail(snail_map):
    snail_map_chain = list(chain.from_iterable(snail_map))
    i = -1
    steps = 0
    dimension = len(snail_map)
    fields = dimension * dimension
    step_limit = dimension
    ret = []

    while True:
        #move right
        while steps<step_limit:
            i+=1
            steps +=1
            ret.append(snail_map_chain[i])
        steps = 0
        step_limit -= 1
        if step_limit == 0: break
        #move down
        while steps<step_limit:
            i += dimension
            steps += 1
            ret.append(snail_map_chain[i])
        steps=0
        #move left
        while steps<step_limit:
            i -= 1
            steps += 1
            ret.append(snail_map_chain[i])
        steps = 0
        step_limit -= 1
        if step_limit == 0: break
        #move up
        while steps<step_limit:
            i -= dimension
            steps += 1
            ret.append(snail_map_chain[i])
        steps = 0

    return ret
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array2 = [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]]
snail(array2)
