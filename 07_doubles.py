import re

def doubles(s):
    re_double = re.compile(r'(.)\1')
    print(re_double.search(s))
    while re_double.search(s):
        s = re_double.sub('', s)
    return s

#print(doubles("aasssdadsdss"))
print(0.1)
