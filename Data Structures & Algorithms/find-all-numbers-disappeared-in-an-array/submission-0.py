class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        actual_nums = range(len(nums) + 1)[1:]
        res = []

        for n in actual_nums:
            if n in nums:
                continue
            res.append(n)
        return res