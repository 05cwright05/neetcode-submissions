class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # given n nodes 0 to n-1
        # given a list of undirected edges (an edge list)
        # Write a function to chck whether those edges make up a valid tree
        # to be a valid tree I would argue we need to check that we need to ensure every node appears in the edge list at least once
        # THus is would be connected and our list of edges is exactly v - 1

        if n == 1 and len(edges)== 0:
            return True
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = deque()

        q.append(0)
        visited.add(0)

        while q:
            curr = q.popleft()

            # add each of our neighbors
            for connected_node in adj[curr]:
                if connected_node not in visited:
                    visited.add(connected_node)
                    q.append(connected_node)

        if len(visited) < n:
            return False
        return True