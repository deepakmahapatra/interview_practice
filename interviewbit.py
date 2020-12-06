
class Solution:

    @staticmethod
    def eval_rpn(arr):
        """Evaluate the value of an arithmetic expression in Reverse Polish Notation.

            Valid operators are +, -, *, /. Each operand may be an integer or another expression.



            Input Format

            The only argument given is character array A.
            Output Format

            Return the value of arithmetic expression formed using reverse Polish Notation.
            For Example

            Input 1:
                A =   ["2", "1", "+", "3", "*"]
            Output 1:
                9
            Explaination 1:
                starting from backside:
                *: ( )*( )
                3: ()*(3)
                +: ( () + () )*(3)
                1: ( () + (1) )*(3)
                2: ( (2) + (1) )*(3)
                ((2)+(1))*(3) = 9

            Input 2:
                A = ["4", "13", "5", "/", "+"]
            Output 2:
                6
            Explaination 2:
                +: ()+()
                /: ()+(() / ())
                5: ()+(() / (5))
                1: ()+((13) / (5))
                4: (4)+((13) / (5))
                (4)+((13) / (5)) = 6
        """
        operations = ['+', '-', '*', '/']
        stack = []
        for item in arr:
            if item not in operations:
                stack.append(float(item))
            else:
                res = None
                item1 = stack.pop()
                item2 = stack.pop()
                if item == "+":
                    res = item2 + item1
                elif item == "-":
                    res = item2 - item1
                elif item == "*":
                    res = item1 * item2
                elif item == "/":
                    res = item2 / item1
                if res:
                    stack.append(res)
        return int(stack.pop())

    def trap(self, arr):
        """
        Problem Description
        
        Given an integer array A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
        
        
        
        Problem Constraints
        1 <= |A| <= 100000
        
        
        
        Input Format
        The only argument given is integer array A.
        
        
        
        Output Format
        Return the total water it is able to trap after raining.
        
        
        
        Example Input
        Input 1:
        
         A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        Input 2:
        
         A = [1, 2]
        """
        left_max = 0
        right_max = 0
        left = 0
        right = len(arr)-1
        water = 0
        while left <= right:
            if arr[left] < arr[right]:
                if arr[left] > left_max:
                    left_max = arr[left]
                else:
                    water += left_max-arr[left]
                left += 1
            else:
                if arr[right] > right_max:
                    right_max = arr[right]
                else:
                    water += right_max-arr[right]
                right -= 1
        return water

    def longest_subsequence(self, array):
        """
        Find the longest increasing subsequence of a given array of integers, A.

        In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order, and in which the subsequence is as long as possible.
        This subsequence is not necessarily contiguous, or unique.
        In this case, we only care about the length of the longest increasing subsequence.


        Input Format:

        The first and the only argument is an integer array A.
        Output Format:

        Return an integer representing the length of the longest increasing subsequence.
        Constraints:

        1 <= length(A) <= 2500
        1 <= A[i] <= 2000
        Example :

        Input 1:
            A = [1, 2, 1, 5]

        Output 1:
            3

        Explanation 1:
            The sequence : [1, 2, 5]

        Input 2:
            A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

        Output 2:
            6

        Explanation 2:
            The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]

        :param A:
        :return:
        """

        def bisect(sub, val):
            low, high = 0, len(sub)-1
            while low <= high:
                mid = (low + high)//2
                if val > sub[mid]:
                    low = mid + 1
                elif val < sub[mid]:
                    high = mid - 1
                else:
                    return mid
            return low
        res = []
        for item in array:
            pos = bisect(res, item)
            if pos == len(res):
                res.append(item)
            else:
                res[pos] = item
        return res

    @staticmethod
    def longest_subsequence_dp(array):
        longest = [1] * len(array)
        if not array:
            return 0
        maximum = 1
        for i in range(1, len(array)):
            for j in range(i):
                if array[i] > array[j]:
                    longest[i] = max(longest[j] + 1, longest[i])
                    maximum = max(longest[i], maximum)
        return maximum


def distinct_subsequences(sequence1, sequence2):
    """
    Given two sequences A, B, count number of unique ways in sequence A, to form a subsequence that is identical
    to the sequence B.

    Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting
    some (can be none) of the characters without disturbing the relative positions of the remaining characters.
    (ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).

    Input Format:

    The first argument of input contains a string, A.
    The second argument of input contains a string, B.
    Output Format:

    Return an integer representing the answer as described in the problem statement.
    Constraints:

    1 <= length(A), length(B) <= 700
    :param sequence:
    :return:
    """
    len1 = len(sequence1)
    len2 = len(sequence2)
    matrix = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    for i in range(1, len1 + 1):
        matrix[0][i] = 1
    for index2 in range(1, len2 + 1):
        for index1 in range(1, len1 + 1):
            if index2 == 1 and index1 == 1:
                if sequence2[index2 - 1] == sequence1[index1 - 1]:
                    matrix[index2][index1] = 1
            else:
                if sequence2[index2 - 1] == sequence1[index1 - 1]:
                    matrix[index2][index1] = matrix[index2][index1 - 1] + matrix[index2 - 1][index1 - 1]
                else:
                    matrix[index2][index1] = matrix[index2][index1 - 1]
    return matrix[len2][len1]


def distinct_subsequences2(S, T):
    m = len(T)
    n = len(S)
    mat = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(n+1):
        mat[0][i] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if T[i-1] != S[j-1]:
                mat[i][j] = mat[i][j-1]
            else:
                mat[i][j] = mat[i-1][j-1] + mat[i][j-1]
    return mat[m][n]


def unique_paths(input_arr):
    """
    Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).

    Now consider if some obstacles are added to the grids. How many unique paths would there be?
    An obstacle and empty space is marked as 1 and 0 respectively in the grid.

    Example :
    There is one obstacle in the middle of a 3x3 grid as illustrated below.

    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    The total number of unique paths is 2.


    :param input_arr:
    :return:
    """
    dp = [[0]*len(input_arr[0])]*len(input_arr)
    # if input_arr[0][0] == 0:
    #     dp[0][0] = 1
    # for i in range(1, len(input_arr)):
    #     if input_arr[i][0] == 0:
    #         dp[i][0] = dp[i-1][0]
    # for j in range(1, len(input_arr[0])):
    #     if input_arr[0][j] == 0:
    #         dp[0][j] = dp[0][j-1]
    # for i in range(1, len(input_arr)):
    #     for j in range(1, len(input_arr[0])):
    #         if input_arr[i][j] == 0:
    #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp


def max_product(arr):
    """
    Find the contiguous subarray within an array (containing at least one number) which has the largest product.
    Return an integer corresponding to the maximum product possible.

    Example :

    Input : [2, 3, -2, 4]
    Return : 6

    Possible with [2, 3]
    :param self:
    :param A:
    :return:
    """
    mnegative = 1
    mpositive = 1
    ans = arr[0]
    for i in arr:
        mnegative, mpositive = min(i, i*mpositive, i*mnegative), max(i, i*mnegative, i*mpositive)
        ans = max(ans, mnegative, mpositive)
    return ans


def possible_decodings(arr):
    """
    Problem Description
    A message containing letters from A-Z is being encoded to numbers using the following mapping:
     'A' -> 1
     'B' -> 2
     ...
     'Z' -> 26
    Given an encoded message A containing digits, determine the total number of ways to decode it modulo 109 + 7.

    Problem Constraints
    1 <= |A| <= 105

    Input Format
    The first and the only argument is a string A.

    Output Format
    Return a single integer denoting the total number of ways to decode it modulo 109 + 7.

    Example Input
    Input 1:

     A = "8"
    Input 2:

     A = "12"
    :param arr:
    :return:
    """
    if len(arr) == 0:
        return 0
    if arr[0] == 0:
        return 0
    n = len(arr)
    result = [0 for _ in range(n+1)]
    result[0] = result[1] = 1
    for i in range(1, n):
        v1 = int(arr[i:i+1])
        v2 = int(arr[i-1:i+1])
        if 0 < v1 <= 9:
            result[i+1] = result[i]
        if 10 <= v2 <= 26:
            result[i+1] = result[i-1] + result[i+1]
        if result[i+1] == 0:
            return 0
    answer = result[n]
    return answer



def match_regex(s, p):
    # m = len(A)
    # n = len(B)
    # if m - A.count('*') - n > 0:
    #     return m - A.count('*') - n != 0
    # dp = [[False for _ in range(n+1)] for _ in range(m+1)]
    #
    # dp[0][0] = True
    # for i in range(1, n+1):
    #     if B[i-1] == "*":
    #         dp[0][i] = dp[0][i-1]
    # for i in range(1, m+1):
    #     for j in range(1, n+1):
    #         if B[j] == "*":
    #             dp[i][j] = dp[i-1][j] or dp[i][j-1]
    #         elif B[j] == "?" or B[j] == A[i]:
    #             dp[i][j] = dp[i-1][j-1]
    #         else:
    #             dp[i][j] = False
    # return dp[m][n]

    if len(p) - p.count('*') > len(s):
        return 0
    DP = [True] + [False]*len(s)
    for c in p:
        if c == '*':
            for n in range(1, len(s)+1):
                DP[n] = DP[n-1] or DP[n]
        else:
            for n in range(len(s)-1, -1, -1):
                DP[n+1] = DP[n] and (c == s[n] or c == '?')
        DP[0] = DP[0] and c == '*'
    return 1 if DP[-1] else 0


# @param A : string
# @return an integer
def minCut(self, A):
    """
    Given a string A, partition A such that every substring of the partition is a palindrome.

    Return the minimum cuts needed for a palindrome partitioning of A.



    Input Format:

    The first and the only argument contains the string A.
    Output Format:

    Return an integer, representing the answer as described in the problem statement.
    Constraints:

    1 <= length(A) <= 501
    Examples:

    Input 1:
        A = "aba"

    Output 1:
        0

    Explanation 1:
    "aba" is already a palindrome, so no cuts are needed.
    Input 2:
    A = "aab"

    Output 2:
        1

    Explanation 2:
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
    :param self:
    :param A:
    :return:
    """
    def isPalin(string):
        for i in range(0, int(len(string)/2)):
            if string[i] != string[len(string)-1-i]:
                return False
        return True

    if len(A) == 0 or len(A) == 1:
        return 0

    min_cuts = [len(A) + 1] * (len(A) + 1)
    min_cuts[0] = 0

    for i in range(1, len(A) + 1):
        if isPalin(A[0:i]):
            min_cuts[i] = 0
        else:
            for j in range(0, i):
                if isPalin(A[j:i]) and min_cuts[j] + 1 < min_cuts[i]:
                    min_cuts[i] = min_cuts[j] + 1

    return min_cuts[len(A)]



def min_path(A):
    """
    Problem Description

    Given a 2D integer array A of size M x N, you need to find a path from top left to bottom right which minimizes the sum of all numbers along its path.

    NOTE: You can only move either down or right at any point in time.



    Input Format
    First and only argument is an 2D integer array A of size M x N.



    Output Format
    Return a single integer denoting the minimum sum of a path from cell (1, 1) to cell (M, N).



    Example Input
    Input 1:

     A = [  [1, 3, 2]
            [4, 3, 1]
            [5, 6, 1]
         ]


    Example Output
    Output 1:

     9
    :param A:
    :return:
    """
    dp = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    dp[0][0] = A[0][0]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i==0 and j==0:
                dp[0][0] = A[0][0]
            elif i==0 and j>0:
                dp[i][j] = dp[i][j-1] + A[i][j]
            elif j>0 and i==0:
                dp[i][j] = dp[i-1][j] + A[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + A[i][j]
    return dp[len(A)-1][len(A[0])-1]


def max_price_cutting_rod(n, prices):
    """
    Given a rod of length n and prices contains price of length i in the array. Find maximum of total revenue you can
    make by cutting and selling the rod
    :param n:
    :param prices:
    :return:
    """
    R = [0] * (n+1)
    for i in range(1, n+1):
        max_val = -1
        for j in range(1, i+1):
            max_val = max(prices[j-1] + R[i-j], max_val)
        R[i] = max_val
    return R[n]


def rob_a_house_rec(n, stashes):
    if n==0:
        return stashes[0]
    max_val = -1
    max_val = max(max_val, rob_a_house_rec(n-1, stashes))
    for i in range(n-2, -1, -1):
        max_val = max(max_val, rob_a_house_rec(i,stashes)+stashes[n-i])
    return max_val


def rob_a_house_db(n, stashes):
    if n==0:
        return stashes[0]
    R = [0] * (n+1)
    R[0] = stashes[0]
    R[1] = max(stashes[0],stashes[1])
    for i in range(2, n+1):
        R[i] = max(R[i-1], stashes[i]+R[i-2]
                   ) #(maximum of not stealing or stealing and adding all other pairs too)

    return R[n]


def longest_common_subsequence(string1, string2):
    dp = [[0 for _ in range(len(string2))] for _ in range(len(string1))]
    if not string1 or not string2:
        return 0
    if string1[0] == string2[0]:
        dp[0][0] = 1
    for i in range(1, len(string1)):
        for j in range(1, len(string2)):
            if string1[i] == string2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(string1)-1][len(string2)-1]


def longest_common_substring(string1, string2):
    dp = [[0 for _ in range(len(string2))] for _ in range(len(string1))]
    if not string1 or not string2:
        return 0
    if string1[0] == string2[0]:
        dp[0][0] = 1
    max_value = -1
    for i in range(1, len(string1)):
        for j in range(1, len(string2)):
            if string1[i] == string2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = 0
            max_value = max(max_value, dp[i][j])
    return max_value


def max_sum_continuous_subarray(array):
    dp = [0 for _ in range(len(array))]
    dp[0] = array[0]
    dp[1] = max(array[1]+dp[0], dp[0], dp[1])
    for i in range(2, len(array)):
        dp[i] = max(dp[i-1]+array[i], array[i])
    return dp[len(array)-1]


def jumps(array):
    length = len(array)-1
    jumps = 0
    reachable = 0
    next_reachable = 0
    for i, x in enumerate(array):
        if reachable >= length:
            break
        if reachable < i:
            reachable = next_reachable
            jumps += 1
            if reachable < i:
                break
            next_reachable = max(next_reachable, i+x)
    return jumps


if __name__ == '__main__':
    print(distinct_subsequences2("abcde", "ab"))
    print(unique_paths([[0, 0, 0, 0, 0, 1, 1, 1, 0, 1],[1, 0, 1, 0, 1, 0, 0, 0, 0, 0],[1, 1, 1, 1, 0, 0, 0, 0, 1, 1]]))
    print(longest_common_subsequence("abcde", "abe"))
    print(longest_common_substring("abcdefghj", "abcefghj"))
    print(max_sum_continuous_subarray([1, 2, 3, -9, 6, 7]))

