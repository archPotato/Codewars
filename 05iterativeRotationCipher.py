
def encode(n,strng):
    workString = strng
    for i in range(abs(n)):
        #memorize spaces and replace them
        spaces = []
        for index in range(len(workString)):
            if workString[index]==" ":
                spaces.append(index)
        strippedStrng = workString.replace(" ", "")

        # shift whole string by n
        shifted_strng = shift(n, strippedStrng)

        #insert spaces
        for index in spaces:
            shifted_strng = shifted_strng[0:index] + " " + shifted_strng[index:]
        substrings = shifted_strng.split(" ")
        recombindedSting = ""

        #recombination

        #print(i+1, substrings)
        #print(i+1, substrings)
        for substr in substrings:
            shifted_substring = shift(n, substr)
            recombindedSting += " " + shifted_substring
        #print(i+1, recombindedSting)
        recombindedSting = recombindedSting.lstrip(" ")
        workString = recombindedSting
    if n>=0:
        workString = str(n) + " " + workString
        #print(recombindedSting)
    return workString

def shift(n, strng):
    shifted_strng = strng
    if len(shifted_strng) >=1:
        if n<0:
            for shift in range(abs(n)):
                shifted_strng = shifted_strng[1:] + shifted_strng[0]
        elif n>0:
            for shift in range(n):
                shifted_strng = shifted_strng[-1] + shifted_strng[0:-1]

    #print(shifted_strng)
    return shifted_strng
def decode(strng):

    #your code goes here. you can do it!
    n = int(strng.split(" ")[0])
    strng = strng.replace(str(n), "").lstrip(" ")

    workString = strng
    for i in range(abs(n)):

        #spaces
        spaces = []
        for index in range(len(workString)):
            if workString[index]==" ":
                spaces.append(index)

        #split in substrings
        substrings = workString.split(" ")

        recombindedSting = ""
        for substring in substrings:
            shifted_substring = shift(-n, substring)
            recombindedSting += shifted_substring
            recombindedSting = recombindedSting.lstrip(" ")

        # shift whole string by -n
        shifted_strng = shift(-n, recombindedSting)

        #insert spaces
        for index in spaces:
            shifted_strng = shifted_strng[0:index] + " " + shifted_strng[index:]
        workString = shifted_strng

    return workString
