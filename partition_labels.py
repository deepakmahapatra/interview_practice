# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
# #
# # Example 1:
# # Input: S = "ababcbacadefegdehijhklij"
# # Output: [9,7,8]
# # Explanation:
# # The partition is "ababcbaca", "defegde", "hijhklij".
# # This is a partition so that each letter appears in at most one part.
# # A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# # Note:
# #
# # S will have length in range [1, 500].
# # S will consist of lowercase letters ('a' to 'z') only.


def partition_label(string_ex):
    dict_with_last_pos = {c: i for i, c in enumerate(string_ex)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(string_ex):
        j = max(j, dict_with_last_pos[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
    return ans

def minSwaps(S):
    n = len(S)
    noOfW = 0

    for i in range(n):
        if (S[i] == 'W'):
            noOfW = noOfW + 1

    x = noOfW

    maxW = -12345678999

    preCompute = {}

    if (S[0] == 'W'):
        preCompute[0] = 1

    for i in range(1, n):
        if (S[i] == 'W'):
            preCompute[i] = preCompute[i - 1] + 1
        else:
            preCompute[i] = preCompute[i - 1]

    for i in range(x - 1, n):
        if (i == (x - 1)):
            noOfW = preCompute[i]
        else:
            noOfW = preCompute[i] - preCompute[i - x]

        if (maxW < noOfW):
            maxW = noOfW

    noOfR = x - maxW

    return noOfR

if __name__ == "__main__":
    print(minSwaps("WRRWWR"))


