def solve(s):
    reversed = s
    #get spáces
    spaces = [i for i in range(len(s)) if s[i]==" "]

    #strip spaces
    reversed = reversed.replace(" ", "")

    #reverse
    reversed = reversed[::-1]

    #add spaces
    for space in spaces:
        reversed = f'{reversed[:space]} {reversed[space:]}'
    return reversed

print(solve("your code rocks"))
