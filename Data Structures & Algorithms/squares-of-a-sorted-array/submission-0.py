class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = deque()
        l, r = 0, len(nums) - 1

        while l <= r:
            left_value = abs(nums[l])
            right_value = abs(nums[r])

            if left_value > right_value:
                result.appendleft(left_value * left_value)
                l += 1
            else:
                result.appendleft(right_value * right_value)
                r -= 1
        return list(result)