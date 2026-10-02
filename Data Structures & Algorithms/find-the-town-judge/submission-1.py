class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # trusts_count = defaultdict(int)
        # trusted_count = defaultdict(int)

        # for trusts, trusted in trust:
        #     trusts_count[trusts] += 1
        #     trusted_count[trusted] += 1
        
        # for i in range(1, n + 1):
        #     if trusts_count[i] == 0 and trusted_count[i] == n -1:
        #         return i

        # return -1 

        trusted_count = defaultdict(int)

        for trusts, trusted in trust:
            trusted_count[trusts] -= 1
            trusted_count[trusted] += 1
        
        for i in range(1, n + 1):
            if trusted_count[i] == n -1:
                return i
        
        return -1