def peak(arr):
    _sum = sum(arr)
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum -arr[i]==(_sum-arr[i])/2:
            return i
        if curr_sum - arr[i]>(_sum-arr[i])/2:
            return -1

print(peak([1,12,3,3,6,3,1]))
