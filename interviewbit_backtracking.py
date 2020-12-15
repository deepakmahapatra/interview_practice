def all_permutations(arr, unique: bool):
    result = []
    all_permutations_helper(arr, 0, len(arr)-1, result, unique)
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


def all_paran(number_brackets_pair):
    answer = []
    all_paran_recur(number_brackets_pair, '', 0, 0, answer)
    return answer


def all_paran_recur(number_brackets_pair,curr, left, right, answer):
    if left == number_brackets_pair and left == right:
        answer.append(curr)
        return
    else:
        if left < number_brackets_pair:
            all_paran_recur(number_brackets_pair, curr + '(', left+1, right, answer)
        if right < left:
            all_paran_recur(number_brackets_pair, curr + ')', left, right+1, answer)


def all_subset(arr):
    result = []
    arr.sort()
    return all_subset_rec(arr, [])


def all_subset_rec(arr, temp):
    yield temp
    if not arr:
        return
    for i in range(len(arr)):
        a = temp.copy()
        a.append(arr[i])
        yield from all_subset_rec(arr[i+1:], a)

# def braces(A):
#     stack = []
#     for i in range(len(A)):
#         if A[i] in '(+-/*':
#             stack.append(A[i])
#         elif A[i] == ')':
#             if stack.pop() == '(':
#                 return 1
#             stack.pop()
#     return 0


def nearest_smaller_less_than_i(arr):
    result = []
    stack = []
    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(num)
    return result


if __name__ == '__main__':
    print([i for i in all_subset([1,2,3])])
    # print(braces('((2+3+5+6))'))
    print(nearest_smaller_less_than_i([1,3,2,5,6]))
