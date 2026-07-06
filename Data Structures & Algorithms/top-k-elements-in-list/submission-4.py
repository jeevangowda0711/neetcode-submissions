class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # tricky bucket sort
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        # count = defaultdict(int)
        # for n in nums:
        #     count[n] += 1
        
        # arr = []
        # for n, c in count.items():
        #     arr.append([c, n])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res