class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we can finish if and only if the class does not have a cycle, so we just need to detect cycles in the graph

        # optimally this can be done with an adjacency list by using a topological sort
        # Topo sort: form adjacency list, create freq_hash_map with the indegrees for each, 
        # loop thru all with indegree = 0 and enqueue them, while the queue is not empty pop
        # reduce the indegree of everything attached to me (store if that was part of question)
        # go thru in degree and if anything aint 0 return as such 

        adjacency_list = {} 

        for prereq in prerequisites:
            if prereq[0] in adjacency_list:
                adjacency_list[prereq[0]].append(prereq[1])
            else:
                adjacency_list[prereq[0]] = [prereq[1]]
        
        freq_map = {}
        print(adjacency_list)
        for key, values in adjacency_list.items():
            if key not in freq_map:
                freq_map[key] = 0
            for connected_node in values:
                if connected_node in freq_map:
                    freq_map[connected_node]+=1
                else:
                    freq_map[connected_node]=1
        q = deque()

        for key, value in freq_map.items():
            if value == 0:
                q.append(key)
        print(freq_map)

        while q: #while it isnt empty
            curr = q.popleft()
            if curr in adjacency_list:
                for connected_node in adjacency_list[curr]: 
                    freq_map[connected_node]-=1
                    if freq_map[connected_node]==0:
                        q.append(connected_node)
        print(freq_map)

        for freq in freq_map.values():
            if freq!=0:
                return False
        return True



