
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

    def distinct_subsequences(self, sequence1, sequence2):
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
        for i in range(len1+1):
            matrix[0][i] = 1
        for index2 in range(len2+1):
            for index1 in range(len1+1):
                if index2 == 1 and index1 == 1:
                    if sequence2[index2 - 1] == sequence1[index1 - 1]:
                        matrix[index2][index1] = 1
                else:
                    if sequence2[index2-1] == sequence1[index1-1]:
                        matrix[index2][index1] = matrix[index2][index1 - 1] + matrix[index2 - 1][index1 - 1]
                    else:
                        matrix[index2][index1] = matrix[index2][index1-1]
        return matrix[len2][len1]
