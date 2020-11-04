# 921. Minimum Add to Make Parentheses Valid
# Medium
#
# 385
#
# 29
#
# Favorite
#
# Share
# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

# Example
# 1:
#
# Input: "())"
# Output: 1
# Example
# 2:
#
# Input: "((("
# Output: 3
# Example
# 3:
#
# Input: "()"
# Output: 0
# Example
# 4:
#
# Input: "()))(("
# Output: 4
#
# Note:
#
# S.length <= 1000
# S
# only
# consists
# of
# '(' and ')'
# characters.


def min_add_to_make_valid(S):
    """
    :type S: str
    :rtype: int
    """
    left = right = 0
    for s in S:
        right += 1 if s == '(' else -1
        if right == -1:
            left += 1
            right += 1
    print(left, right)
    return left + right


# def min_add_to_make_valid1(s):
#     # n = s.length
#     curr_sum = 0
#     summ_track = 0
#
#     for i in s:
#         if i=="(":
#             curr_sum+=1
#             summ_track+=1
#         else:
#             if summ_track<=0:
#                 curr_sum+=1
#             else:
#                 summ_track-=1
#                 curr_sum-=1
#     return curr_sum

def merge(A, B):
    start_a, start_b = 0, 0
    result = []
    while start_a < len(A) and start_b < len(B):
        if A[start_a] > B[start_b]:
            result.append(B[start_b])
            start_b += 1
        else:
            result.append(A[start_a])
            start_a += 1

    while start_a < len(A):
        result.append(A[start_a])
        start_a += 1
    while start_b < len(B):
        result.append(B[start_b])
        start_b += 1
    return result

def is_matched_expression(expr):
    result = list()
    left = '({['
    right = ')}]'
    for char in expr:
        if char in left:
            result.append(char)
        elif char in right:
            if len(result) == 0:
                return False
            if right.index(char) != left.index(result.pop()):
                return False
    return len(result) == 0

if __name__ == "__main__":
    print(min_add_to_make_valid("())))()"))
    print(merge([-4, 3], [-2, -2 ]))
    print(is_matched_expression("{}]"))
    print(is_matched_expression("[{}()]"))
