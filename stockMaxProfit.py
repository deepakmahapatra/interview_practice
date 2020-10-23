"""
Problem:
- Given a list of stock prices (integer) in chronological order, return the
  max profit from buying at earlier time and selling at later time.
Example:
- Input: []int{10, 7, 5, 8, 11, 9}
  Output: 6, because one can buy at 5 and sell at 11
Approach:
- Use a greedy approach to keep track of the minimum price and the maximum
  profit for each value while iterating through the list.
Solution:
- Initialize a minimum price to be the first price in the list and a maximum
  profit to be the first possible profit that we could trade.
- Iterate through the list and keep track of:
  - the current price
  - the potential profit: current price - minimum price
  - the maximum profit: the larger profit between the current maximum and the potential one
  - the minimum price: the smaller price between the current minimum and the current price.
- Return the maximum profit we found in the end.
Cost:
- O(n) time, O(1) space.
"""
import math


def max_profit(stocks):
    if stocks:
        min_price = stocks[0]
        max_profit_ = stocks[1]-stocks[0]
        for current_price in stocks:
            potential_profit = current_price - min_price
            max_profit_ = max(potential_profit, max_profit_)
            min_price = min(min_price, current_price)
        return max_profit_
    else:
        return 0


if __name__ == "__main__":
    print(max_profit([10, 7, 5, 8, 11, 9]))
