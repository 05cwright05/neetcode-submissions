class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force would be to start at the beginning and tehn see how farwe can go without repeating a characgter
        # to speed this up we could add them to a hash map as we go
        # and if they exist in that hashmap then it is a duplicate and move on starting from the neext char instaad
        # I am wondering if we can do something with a sldiing window here
        # i.e. i continue expanding until i reach a repeated character 
        # if i reacha repeated character then i should move my left pointer by one
        # if my right pointer reaches the end we know we are done since it cant get any longer than stating at beginning and eraching end
        # in the worst case we would have the longest subsequence be the last 2
        # i.e. xxxxx xxxxxy in this case to prevent this 
        #dont need to cuz left pointer moves ahead as soon as we see it
        # bu thten i have to consder xyxyxyx xyxyxyz
        # this could definitely work
        # i am not sure what time complexity is here
        # if its all one sequence then we do it in O(n) time
        # suppose we have xxxxy then we visit x,x x,x x,x x,x, x,y or O(2n)
        # suppose we have xyzxyz then we visit x,y,z y,z,x z,x,y or O(3n)
        # suppose we have xxxxxx (O(n))
        # so in the worst case i think it is O(26n perhaps) or O(n)

        left = 0
        right = 0
        best_length = 0
        while left < len(s):
            my_map = {}
            curr_length = 0
            while right < len(s):
                if my_map.get(s[right]): # already in subsequence
                    best_length = max(best_length, curr_length)
                    break
                else:
                    my_map[s[right]] = 1
                    right+=1
                    curr_length += 1
            best_length = max(best_length, curr_length) # in case we hit the end'
            left+=1
            right=left
        return best_length