def dots_and_boxes(ar):
    ar = sort_tuples(ar)
    player_1 = True
    count = [0,0]
    dimension = get_dimension(ar)

    for i, line in enumerate(ar):
        #print(check_square(line, ar[0:i], dimension))
        if check_square(line, ar[0:i], dimension):
            count[~player_1] +=1
        else:
            player_1 = not player_1
    print(count)
    return (count[0], count[1])

def check_square(turn, ar, dim):
    #horizontal
    if abs(turn[0]-turn[1])==1:
        #up
        if (turn[0]-dim, turn[1]-dim) in ar and (turn[0]-dim, turn[0]) in ar and (turn[1]-dim, turn[1]) in ar:
            return True
        #down
        elif (turn[0]+dim, turn[1]+dim) in ar and (turn[0]+dim, turn[0]) in ar and (turn[1]+dim, turn[1]) in ar:
            return True
        else:
            return False
    else:
        if (turn[0]+1, turn[1]+1) in ar and (turn[0], turn[0]+1) in ar and (turn[1], turn[1]+1) in ar:
            return True
        elif (turn[0]-1, turn[1]-1) in ar and (turn[0]-1, turn[0]) in ar and (turn[1]-1, turn[1]) in ar:
            return True
        else:
            return False

def sort_tuples(ar):
    ret = []
    for tup in ar:
        ret.append((tup[0], tup[1]))
        if tup[1]<tup[0]:
            ret.append((tup[1],tup[0]))
    return tuple(ret)

def get_dimension(ar):
    for i in ar:
        if abs(i[0]-i[1])>1:
            return abs(i[0]-i[1])

dots_and_boxes(((0,1),(7,8),(1,2),(6,7),(0,3),(5,8),(3,4),(1,4),(4,5),(2,5),(4,7),(3,6)))
