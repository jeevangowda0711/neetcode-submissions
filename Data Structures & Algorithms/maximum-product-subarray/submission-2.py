class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = nums[0]

        # for i in range(len(nums)):
        #     cur = nums[i]
        #     res = max(res, cur)
        #     for j in range(i + 1, len(nums)):
        #         cur *= nums[j]
        #         res = max(res, cur)
        # return res
        
        res = nums[0]
        curMax, curMin = 1, 1

        for n in nums:
            temp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
        return res