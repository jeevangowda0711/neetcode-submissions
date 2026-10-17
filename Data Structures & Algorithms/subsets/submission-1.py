class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, subset):
            result.append(subset[:])
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
            
        backtrack(0, [])
        return result
        
        # result = []

        # subset = []
        # def backtrack(i):
        #     if i >= len(nums):
        #         result.append(subset[:])
        #         return
            
        #     subset.append(nums[i])
        #     backtrack(i + 1)

        #     subset.pop()
        #     backtrack(i + 1)
        
        # backtrack(0)
        # return result
        