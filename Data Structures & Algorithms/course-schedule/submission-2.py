class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}

        for c in range(numCourses):
            graph[c] = []
        
        for edge in prerequisites:
            a, b = edge
            graph[a].append(b)
        
        def dfs(node):
            if node in visited:
                return False
            if graph[node] == []:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(node)
            graph[node] = []
            
            return True

        visited = set()

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True