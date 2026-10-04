class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        l = 0
        current_length = 0
        for r in range(len(nums)):
            current_length += nums[r]
            while current_length >= target:
                min_length = min(min_length, r - l + 1)
                current_length -= nums[l]
                l += 1
                
        if min_length == float('inf'):
            return 0
        return min_length