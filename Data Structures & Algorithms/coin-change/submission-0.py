class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin_req_for_idx = [amount + 1] * (amount + 1)
        min_coin_req_for_idx[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if (i - coin) >= 0:
                    min_coin_req_for_idx[i] = min(min_coin_req_for_idx[i], 1 + min_coin_req_for_idx[i - coin])
        return min_coin_req_for_idx[amount] if (min_coin_req_for_idx[amount] != amount + 1) else -1