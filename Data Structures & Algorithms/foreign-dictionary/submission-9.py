class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        adjacency_map = {} # goes from letter to a set of letters taht it points to
        unique_letters = set()
        for i in range(0, len(words)-1): 
            for j in range(i+1, len(words)): # loop through all words for each word
                word1 = words[i]
                word2 = words[j]
                for z in range(0, len(word1)):
                    unique_letters.add(word1[z])

                for z in range(0, len(word2)):
                    unique_letters.add(word2[z])

                    
                found_diff = False
                for z in range(0, min(len(word1), len(word2))):
                    if word1[z] == word2[z]:
                        continue
                    elif word1[z] != word2[z]:
                        # add to our adjacency list
                        if word1[z] in adjacency_map:
                            adjacency_map[word1[z]].add(word2[z])
                        else:
                            adjacency_map[word1[z]] = set({word2[z]})
                        found_diff = True
                        break # once we have added a letter the other letters dont have a meaningful relationship
                if not found_diff:
                    if len(word1) > len(word2):
                        return ""

        # perform topological sort on our build graph
        #kahns algorithm

        # step 1 find the indegree of each word
        indegrees = {}

        for key, values in adjacency_map.items():
            if key not in indegrees:
                indegrees[key] = 0
            for value in values:
                if value not in indegrees:
                    indegrees[value] = 1
                else:
                    indegrees[value]+=1
        print(adjacency_map)

        print(indegrees)
        q = deque()

        # now enque all values with an indegree of 0
        for key,value in indegrees.items():
            if value == 0:
                q.append(key)


        output = ""
        while q: # while its not empty
            curr = q.popleft()
            output+=curr
            if curr in adjacency_map:
                set_of_edges = adjacency_map[curr]
                for edge in set_of_edges:
                    indegrees[edge]-=1
                    if indegrees[edge] == 0:
                        q.append(edge)


        # check to see if its valid
        for value in indegrees.values():
            if value > 0:
                return ""
        
        for letter in unique_letters:
            if letter not in output:
                output+=letter

        return output
