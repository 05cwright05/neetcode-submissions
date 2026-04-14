class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_left = 0
        best_right = math.inf

        left = 0
        right = 0

        a_s = {}
        a_t = {}
        print("starting")

        for char in t:
            if char not in a_t:
                a_t[char] = 1
            else:
                a_t[char]+=1
        
        while right < len(s):
            char_considering = s[right]
            if char_considering not in a_s:
                a_s[char_considering] = 1
            else:
                a_s[char_considering] += 1

            # max of 52 values so technically O(n) tho
            valid_substring = True
            for key, value in a_t.items():
                if key not in a_s:
                    valid_substring = False
                    break
                elif a_s[key] < value:
                    valid_substring = False
                    break
            if valid_substring:
                # move left forward as much as possible
                while True:
                    considering_removing = s[left]
                    if considering_removing not in a_t or a_t[considering_removing] < a_s[considering_removing]:
                        a_s[considering_removing]-=1
                        left+=1
                    else:
                        break
                current_size = best_right - best_left + 1
                if right - left + 1 < current_size:
                    best_right = right
                    best_left = left
            right+=1
        print("done")
        if best_right == math.inf:
            print("RETRUNING NOTHING BURRE\n")
            return ""
        else: 
            print("Returning \n", s[best_left:best_right+1])
            return s[best_left:best_right+1]
