import math


def max_profit(prices: list[int]) -> int:
    min_price = math.inf
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def max_profit_two_pointers(prices: list[int]) -> int:
    # Edge case
    if not prices or len(prices) < 2:
        return 0

    max_profit = 0
    left_buy, right_sell = 0, 1

    while right_sell < len(prices):
        current_price = prices[right_sell]
        buy_price = prices[left_buy]

        if buy_price > current_price:
            current_profit = current_price - buy_price
            max_profit = max(max_profit, current_profit)
        else:
            left_buy = right_sell

        right_sell += 1

    return max_profit
