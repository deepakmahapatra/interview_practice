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

def next_permutation(nums):
    i = len(nums)-2
    while i >=0 and nums[i+1] <= nums[i]:
        i-=1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j-=1
        nums[i], nums[j] = nums[j], nums[i]
    j = len(nums) - 1
    i += 1
    while i <j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums


def should_swap(arr, l, current):
    for i in range(l, current):
        if arr[i] == arr[current]:
            return False
    return True


def combination(n, k):
    def recur(output, n, k, first=1, curr=[]):
        if len(curr) == k:
            output.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                recur(output, n, k, i, curr)
                curr.pop(i)
        output = []
        recur(output, n, k)
        return output


def all_paran(number_brackets_pair):
    answer = []
    all_paran_recur(number_brackets_pair, '', 0, 0, answer)
    return answer


def all_paran_recur(number_brackets_pair, curr, left, right, answer):
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


def word_break(s, word_dict):
    memo = {}

    return word_break_rec(s, word_dict, memo)


def word_break_rec(s, word_dict, memo):
    if s in memo:
        return memo[s]
    if not s:
        return []
    res = []
    for word in word_dict:
        if not s.startswith(word):
            continue
        if len(s) == len(word):
            res.append(word)
        else:
            rest_strings = word_break_rec(s[len(word):], word_dict, memo)
            for rest in rest_strings:
                rest = word + ' ' + rest
                res.append(rest)
    memo[s] = res
    return res


def is_palindrome_del_one_chars(s):
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            if is_palindrome(s, start+1, end):
                return True
            if is_palindrome(s, start, end-1):
                return True
            return False
    return True


def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def longest_palindrome_substring(s):
    ans = ''
    longest = 0
    n = len(s)
    dp = [[0] * n for _ in range(len(s))]
    for i in range(n):
        dp[i][i] = 1
        longest = 1
        ans = s[i]
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            ans = s[i:i+2]
            longest = 2

    for j in range(n):
        for i in range(j-1):
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if longest < j-i+1:
                    longest = j-i+1
                    ans = s[i: j+1]
    return ans





def min_deletion_to_make_string_palindrome(string):
    return util_for_deletion(string, 0, len(string) - 1)


def util_for_deletion(string, start, end):
    if start >= end:
        return
    if string[start] == string[end]:
        return util_for_deletion(string, start+1, end-1)
    return 1 + min(util_for_deletion(string, start+1, end), util_for_deletion(string, start, end-1))


if __name__ == '__main__':
    print([i for i in all_subset([1,2,3])])
    # print(braces('((2+3+5+6))'))
    print(nearest_smaller_less_than_i([1,3,2,5,6]))
    print(word_break("thisisaword", {"this", "is", "a", "word", "dict"}))

    print(is_palindrome_del_one_chars("abca", 0))
    print(is_palindrome_del_one_chars("abdca", 3))

    print("\nLength is: ", longest_palindrome_substring("forgeeksskeegfor"))
