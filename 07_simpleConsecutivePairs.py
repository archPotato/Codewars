def pairs(ar):
    count = 0
    for i in range(0,len(ar),2):
        if i+1 < len(ar):
            if abs(ar[i] - ar[i+1])==1:
                count +=1
    return count


#iterate as pairs with zip()
def pairs(arr):
    count = 0
    for a,b in zip(arr[::2],arr[1::2]):
        if (abs(a-b)==1):
            count += 1
    return count

    #return sum( abs(a-b)==1 for a,b in zip(arr[::2],arr[1::2]) )

#use list comprehension and sum()
#sum takes the sum of an iterable, counts True as 1
def pairs(arr):
    consecutives = [abs(a-b)==1 for a,b in zip(arr[::2],arr[1::2])]
    return sum(consecutives)

print(pairs([1,2,5,8,-4,-3,7,6,5]))
