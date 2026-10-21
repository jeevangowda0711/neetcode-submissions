class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for src, dst in edges:
            incoming[dst] += 1
        
        champions = []

        for i, incoming_count in enumerate(incoming):
            if not incoming_count:
                champions.append(i)
        
        if len(champions) > 1:
            return -1
        else:
            return champions[0]