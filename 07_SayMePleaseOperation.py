def say_me_operations(string_numbers):
    numbers = list(map(int, string_numbers.split(" ")))
    ret = ""
    for a, b, c in zip(numbers[:], numbers[1:], numbers[2:]):
        if a + b == c:
            ret = " ".join((ret, "addition"))
        elif a-b == c:
            ret = " ".join((ret, "substraction"))
        elif a/b == c:
            ret = " ".join((ret, "division"))
        elif a*b == c:
            ret = " ".join((ret, "multiplication"))
    return ret

print(
say_me_operations("1 2 3 5 8")
)
