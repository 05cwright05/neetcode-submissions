class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # suppose we create a hashmap of size 26 1 spot for each character
        # when we see a new character we up it in the hash_map
        # if we see a value is greater than 1 we decrement length of substring and remove the ones we are popping out
        # until we get to ourself
        # as we go we maintain the best one we have seen


        # in a loop
        # advance right pointer forward
        # if not in map add to map
        # if in map then that means its a duplicate
        # move left pointer and each time it moves decrement its previous location from the map
        # stop once s[target] == 1 again aka we moved away from the character that was the problem
        # then continue moving right

        left = 0
        right = 0

        my_map = {}
        best_length = 0
        curr_count = 0
        while right < len(s):
            if not my_map.get(s[right]):
                my_map[s[right]] = 1
            else:
                my_map[s[right]]+=1
                # already in it we need to move left until we find it
                while my_map[s[right]] > 1:
                    my_map[s[left]] -= 1 #decrement the map where l is
                    left+=1 # move left forward
            best_length = max(right -left+1, best_length)
            right+=1

        return best_length
            
