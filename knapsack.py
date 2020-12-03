def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                   knapSack(W, wt, val, n - 1))


def knapSackDP(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n):
        for j in range(1, W+1):
            if j-wt[i] >= 0 and (val[i]+dp[i-1][j-wt[i]] > dp[i-1][j]):
                dp[i][j] = val[i] + dp[i-1][j-wt[i]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n-1][W]
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapSackDP(W, wt, val, n))
    print(knapSack(W, wt, val, n))
