class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # seen = set()
        # for i, n in enumerate(nums):
        #     if n in seen:
        #         return True
        #     seen.add(n)
        #     if len(seen) > k:
        #         seen.remove(nums[i - k])
        # return False
        seen = {}
        for i, n in enumerate(nums):
            if n in seen and i - seen[n] <= k:
                return True
            seen[n] = i
        return False