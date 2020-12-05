def ips_between(start, end):
    start, end = start.split("."), end.split(".")
    start_bin, end_bin = parseIPasDecimal(start), parseIPasDecimal(end)

    return abs(end_bin - start_bin)

def parseIPasDecimal(ip):
    binary = []
    for i in ip:
        temp = (f'{"{0:b}".format(int(i))}')
        if temp[0]=='1':
            temp = temp.zfill(8)
        else:
            temp = temp.ljust(8, '0')
        binary.append(temp)
    return int("".join(binary), 2)

print(
    ips_between("10.0.0.0", "10.0.0.50")
)
