class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin_array = [math.inf] * (amount + 1)
        min_coin_array[0] = 0
        for min_coin_amount in range(1, amount + 1):
            for coins_value in coins:
                if min_coin_amount >= coins_value and min_coin_array[min_coin_amount - coins_value] != -1:
                    min_coin_array[min_coin_amount] = min(min_coin_array[min_coin_amount], min_coin_array[min_coin_amount - coins_value] + 1)
            if min_coin_array[min_coin_amount] == math.inf:
                min_coin_array[min_coin_amount] = -1
        return min_coin_array[amount]