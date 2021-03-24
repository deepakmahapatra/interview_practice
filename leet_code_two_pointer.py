import bisect


def findClosestKItems(arr, k, x):
    n = len(arr)
    if arr[0] >= x:
        return arr[:k]
    if arr[n-1] <= x:
        return arr[n-k:]
    index = bisect.bisect(arr, x)
    if index < 0:
        index = -index-1
    low = max(0, index - k - 1)
    high = min(n-1, index + k -1)
    while high - low > k - 1:
        if low <0 or (x - arr[low]) <= (arr[high]-x):
            high += 1
        elif high >= n or (x-arr[low]) > (arr[high]-x):
            low -= 1
    return arr[low: high+1]


