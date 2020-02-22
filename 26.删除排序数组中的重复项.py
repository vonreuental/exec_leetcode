#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:return 0
        count = 0
        for i in range(1, len(nums)):
            if nums[count] != nums[i]:
                nums[count + 1] = nums[i]
                count +=1
        return count + 1
