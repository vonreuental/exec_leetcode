#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dpI0 = [0] * 3
        dpI1 = [float('-INF')] + [- prices[0]] * 2 
        for i in range(1, len(prices)):
            for k in range(1, 3):
                dpI0[k] = max(dpI0[k], dpI1[k] + prices[i])
                dpI1[k] = max(dpI1[k], dpI0[k - 1] - prices[i])
        return dpI0[2]
# @lc code=end

