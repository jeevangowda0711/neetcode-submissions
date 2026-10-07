class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # l = 0
        # r = len(nums) - 1
        # result = []

        # while l <= r:
        #     a = nums[l] * nums[l]
        #     b = nums[r] * nums[r]

        #     if a > b:
        #         result.append(a)
        #         l += 1
        #     else:
        #         result.append(b)
        #         r -= 1
        
        # return result[::-1]
        l, r = 0, len(nums) - 1
        result = []
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1
        return result[::-1]