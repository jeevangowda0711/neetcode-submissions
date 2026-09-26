class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # actual_nums = range(1, len(nums) + 1)
        # res = []

        # for n in actual_nums:
        #     if n in nums:
        #         continue
        #     res.append(n)
        # return res
        # store = set(range(1, len(nums) + 1))

        # for n in nums:
        #     store.discard(n)

        # return list(store)
        store = set(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in store:
                res.append(i)
        return res