def max_k_unique(arr, k):
    count = start = end = 0
    n = len(arr)
    unique_cnt = {}

    while end < n:
        if arr[end] not in unique_cnt:
            unique_cnt[arr[end]] = 0
        unique_cnt[arr[end]] += 1

        while len(unique_cnt) > k:
            unique_cnt[arr[start]] -= 1
            if unique_cnt[arr[start]] == 0:
                del unique_cnt[arr[start]]
            start += 1

        count += end - start + 1
        end += 1
    return count


def exact_k_unique(arr, k):
    return max_k_unique(arr, k) - max_k_unique(arr, k-1)


if __name__ == '__main__':
    arr = ['a', 'b', 'c', 'a', 'b']
    assert exact_k_unique(arr, 3) == 6
    arr = [1, 2, 1, 2, 3]
    assert exact_k_unique(arr, 2) == 7
