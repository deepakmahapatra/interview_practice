def all_permutations(arr, unique:bool):
    result = []
    all_permutations_helper(arr, 0, len(arr)-1, result, bool)
    return result

def all_permutations_helper(arr, l, r, result, unique):
    if l == r:
        result.append(arr.copy())
    for i in range(l, r+1):
        swap = True
        if unique:
            if not should_swap(arr, l, i):
                swap = False
        if swap:
            arr[i], arr[l] = arr[l], arr[i]
            all_permutations_helper(arr, l+1, r, result, unique)
            arr[i], arr[l] = arr[l], arr[i]


def should_swap(arr, l, current):
    for i in range(l, current):
        if arr[i] == arr[current]:
            return False
    return True
