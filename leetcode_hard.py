# On a 2-dimensional grid, there are 4 types of squares:
#
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
from typing import List


class UniquePath:
    def __init__(self):
        pass
    def unique_paths(self, grid: List[List[int]]):
        if not grid:
            return 0
        count=0
        start_x, start_y = 0, 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                if grid[i][j] == 1:
                    start_x, start_y = i, j
        return self.backtrack(start_x, start_y, count, m, n, grid)

    def backtrack(self, start_x, start_y, count, m, n, grid):
        if start_x == m or start_x < 0 or start_y < 0 or start_y == n or grid[start_x][start_y] == -1:
            return 0
        if grid[start_x][start_y] == 2:
            return int(count == 1)
        res = 0
        grid[start_x][start_y] = -1
        for i, j in [(start_x+1, start_y), (start_x, start_y+1), (start_x-1, start_y), (start_x, start_y-1)]:
            res += self.backtrack(i, j, count-1, m, n, grid)
        grid[start_x][start_y] = 0
        return res

    def median_of_two_sorted_array(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.median_of_two_sorted_array(nums2, nums1)
        x = len(nums1)
        y = len(nums2)
        low = 0
        high = x
        while low <= high:
            part_x = (low + high)//2
            part_y = (x+y+1) - part_x

            max_left_x = float('-inf')  if part_x ==0 else nums1[part_x-1]
            min_right_x = float('inf')  if part_x ==x else nums1[part_x]

            max_left_y = float('-inf')  if part_y ==0 else nums2[part_y-1]
            min_right_y = float('inf')  if part_y ==y else nums2[part_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x+y) % 2 == 0:
                    return (max(max_left_y, max_left_x) + min(min_right_x, min_right_y))/2.0
                return max(max_left_y, max_left_x)
            elif max_left_x > min_right_y:
                high = part_x - 1
            else:
                low = part_x + 1
