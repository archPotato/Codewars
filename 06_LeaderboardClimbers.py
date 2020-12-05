# def leaderboard_sort(leaderboard, changes):

#     new_leaderboard = leaderboard

#     for name, val in map(str.split, changes):
#         oldIndex = new_leaderboard.index(name)
#         new_leaderboard.remove(name)
#         new_leaderboard.insert(oldIndex-int(val), name)
#     return new_leaderboard

def leaderboard_sort(lbd, changes):
    lbd = lbd[:]
    for name,n in map(str.split, changes):
        n,i = int(n), lbd.index(name)
        lbd.pop(i)
        lbd.insert(i-n,name)
    return lbd

print(
    leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1'])
)
