class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Given a graph of n nodes

        Given an integer n
        Given array edges where edge(u,v) means there is an edge between u and v
        Return the number of connected components


        Here is what I am thinking
        We maintain a map of visited
        We run bfs on each of the nodes lsited in the edge (obviously nothing happens if it has already been visited)

        But to make it easier we build an adjacency list from the edge list
        Then run bfs with that and mark them as we go. Each time we find an unvisited one we increment a counter

        So bascially:
        1. Create adjacency_map
        2. Create global visited list
        3. Loop through adjacency list keys
            - Check if has been visited
            - increment our conter by 1
            - Enqueue if not and mark visited
                - while the queue is not empty
                - Enqqueue and makr any neigbors we can reach as visited
        4. return out count

        """
        adjacency_map = {}
        for edge in edges:
            if edge[0] not in adjacency_map:
                adjacency_map[edge[0]] = [edge[1]]
            else:
                adjacency_map[edge[0]].append(edge[1])

            if edge[1] not in adjacency_map:
                adjacency_map[edge[1]] = [edge[0]]
            else:
                adjacency_map[edge[1]].append(edge[0])

        visited = {}
        count = 0
        q = deque()

        for key in adjacency_map:
            if key not in visited:
                count+=1
                q.append(key)
                visited[key] = True
                while q:
                    curr = q.popleft()
                    for connected_node in adjacency_map[curr]:
                        if connected_node not in visited:
                            q.append(connected_node)
                            visited[connected_node] = True

        number_considered = len(adjacency_map)
        count += (n - number_considered) # each taht we have not considered must be its own
        return count


            
