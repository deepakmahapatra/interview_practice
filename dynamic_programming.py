def count_no_of_ways_to_climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_no_of_ways_to_climb_stairs(n - 1) + count_no_of_ways_to_climb_stairs(n - 2)


def count_no_of_ways_to_climb(n):
    s = []
    s.append(0)
    s.append(1)
    s.append(2)
    for i in range(3, n + 1):
        s.append(s[i - 1] + s[i - 2])
    return s[n]


def num_decodings(string):
    dp = [0 for _ in range(len(string) + 1)]
    if not string:
        return 0

    dp[0] = 1
    dp[1] = 1 if string[0] != "0" else 0
    for i in range(2, len(string) + 1):
        if string[i - 1] != "0":
            dp[i] = dp[i - 1]
        two_digit = int(string[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    return dp[len(string)]


def maximum_square_area_with_1(matrix):
    """
    given a matrix find out the maximum square area that can be formed with cells 1
    Args:
        matrix:

    Returns:

    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    answer = 0
    dp = [[0 for _ in range(cols+1)] * (rows+1)]
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i][j]) + 1
                answer = max(answer, dp[i][j])

    return answer * answer

if __name__ == '__main__':
    print(count_no_of_ways_to_climb_stairs(5))
    print(count_no_of_ways_to_climb(5))
