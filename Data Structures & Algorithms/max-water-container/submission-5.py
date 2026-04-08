class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we are given an array of heights
        # these heights represent the height of a bar that I could choose to place there
        # to maximize height we need to maximize distance apart and height

        # gotta ne some kind of 2 pointer / sliding window problem

        # essentially i start with left pointer at index 0 and right pinter at index 1, then i move my right pointer froward and recrod the total volume

        # naive approach if for each left wall try every possible right wall i.e. n^2

        # waht if we knew the best capacity we could make at each spot like a suffix sum array with respect to the beginning
        # key observation: we will never choose a lower bar for our left ;ointer
        # that is we can do a lot of skipping
        # so for the first one we choose the very first height, but after taht we jumkp the left point to the right pointer
        # if right is > left. Becuase imagine that if you are moving along i wouold never start more right at a lower point
        # i may start more right only if it increases the height

        # the worst case here is strictly descending heights - but do you think it would be appropriate to code up what we have right now
        # or should i keep thinking on it

        left = 0
        right = len(heights)-1
        best_volume = 0
        while left < right:
            best_volume = max(best_volume, (right-left)*min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return best_volume