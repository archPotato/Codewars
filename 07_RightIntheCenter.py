def is_in_middle(sequence):
    i = 0
    for a,b,c in zip(sequence, sequence[1:], sequence[2:]):
        i+=1
        if a+b+c == "abc":
            if abs((i-1)-(len(sequence)-i-2))<=1:
                return True
    return False


print("AAAabcabcBBB".find("abc"))
