class Solution:

    def diff_possible(self, A, B):
        """
        Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

         Example: Input :
            A : [1 3 5]
            k : 4
         Output : YES as 5 - 1 = 4
            Return 0 / 1 ( 0 for false, 1 for true ) for this problem
        :param A:
        :param B:
        :return:
        """
        left, right = 0, 1
        while left <= right < len(A):
            diff = A[right] - A[left]
            if diff < B or left == right:
                right += 1
            elif diff > B:
                left += 1
            else:
                return 1
        return 0

    @staticmethod
    def intersection_two_sorted_array(A, B):
        """
        Find the intersection of two sorted arrays.
        OR in other words,
        Given 2 sorted arrays, find all the elements which occur in both the arrays.

        Example :

        Input :
            A : [1 2 3 3 4 5 6]
            B : [3 3 5]

        Output : [3 3 5]

        Input :
            A : [1 2 3 3 4 5 6]
            B : [3 5]

        Output : [3 5]
        :param A:
        :param B:
        :return:
        """
        lstart = rstart = 0
        result = []
        while lstart < len(A) and rstart < len(B):
            if A[lstart] < B[rstart]:
                lstart += 1
            elif A[lstart] > B[rstart]:
                rstart += 1
            else:
                result.append(A[lstart])
                lstart += 1
                rstart += 1
        return result

    @staticmethod
    def merge(A, B):
        """
        Given two sorted integer arrays A and B, merge B into A as one sorted array.

         Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
        TIP: C users, please malloc the result into a new array and return the result.
        If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

        Example :

        Input :
                 A : [1 5 8]
                 B : [6 9]

        Modified A : [1 5 6 8 9]
        """
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

    @staticmethod
    def threesum_closest(arr, target):
        arr.sort()
        closest = None
        for i in range(len(arr)-2):
            j, k = i+1, len(arr)-1
            while k > j:
                three_sum = arr[i] + arr[j] + arr[k]
                if three_sum == target:
                    return three_sum
                if not closest or abs(target-closest) > abs(target-three_sum):
                    closest = three_sum
                if three_sum < target:
                    j += 1
                else:
                    k -= 1
        return closest





