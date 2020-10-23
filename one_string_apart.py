# Problem:
# - Given two strings, determine if they are both one edit distance apart.
# Example:
# - Input: "abcde", "abXde"
#   Output: true
#   Explanation: Only "c" in S is replaced by "X" in T.
# - Input: "abcde", "abcXde"
#   Output: true
#   Explanation: "X" is inserted between "c" and "d" in S to get T.
# Approach:
# - Use two-pointer approach to traverse both strings at the same time and
#   keep track of count of difference characters.
# Solution:
# - If the difference between lengths of two strings is more than 1, return
#   false immediately because they are not at one distance anyway.
# - Iterate through both string at the same time and move both pointers up
#   their corresponding characters match as follow:
#   - If the length of one string is more than the other, a possible edit is
#     to remove a character. We move the pointer in the larger string up.
#   - If they are the same length, a possible edit is to change a character.
#     In that case, simply move both of them up.
#   - Remember to increment the edit count.
# - If the character is extra in any string, also increment the edit count.
# Cost:
# - O(n) time, O(1) space


def one_string_apart(string1, string2):
    if len(string1)-len(string2) > 1:
        return False
    count = 0
    i = j = 0
    m = len(string1)
    n = len(string2)
    while i < m and j < n:
        if string1[i] != string2[j]:
            if count == 1:
                return False
            if m < n:
                j += 1
            elif m > n:
                i += 1
            else:
                i += 1
                j += 1

            count += 1
        i += 1
        j += 1
    if i < m or j < n:
        count += 1
    if count == 1:
        return True
    return False


if __name__ == "__main__":
    print(one_string_apart("abcde", "abXde"))

