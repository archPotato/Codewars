def two_oldest_ages(ages):
    first_max = max(ages)
    ages.remove(first_max)
    sec_max = max(ages)
    return [sec_max, first_max]

print(two_oldest_ages([1,3,5,6]))
