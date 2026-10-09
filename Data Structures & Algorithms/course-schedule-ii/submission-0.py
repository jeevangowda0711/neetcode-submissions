class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c:[] for c in range(numCourses)}
        for edge in prerequisites:
            a,b = edge
            graph[a].append(b)

        def dfs(node):
            res = []
            if node in visited:
                return True
            if node in cycle:
                return False

            cycle.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor) == False:
                    return False
            cycle.remove(node)
            visited.add(node)
            result.append(node)
            return True

        result = []
        visited = set()
        cycle = set()
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return result