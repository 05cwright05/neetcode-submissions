class Solution:
    def rob(self, nums: List[int]) -> int:
        # so we are given a list of houses each with an associated value
        # we want to maximazie the total value we can collect
        # however we can never visit 2 houses that are next to each other
        # i.e. if i pick house 1 i can not have house 2, but if i pick house 2 i cannot have house 1 or 3.
        # so im 

        # at each step we could savve the max amount of money we could have up to that house
        # then we could decide at each step whether to take myself + the value 1 before or take the previous value

        dp_array = [0 for _ in range(0, len(nums)+2)]
        dp_array[0] = 0 #prev prev
        dp_array[1] = 0 #prev

        for i in range(0, len(nums)):
            dp_array[i+2] = max(dp_array[i]+nums[i], dp_array[i+1])

        print(dp_array)
        return dp_array[-1]
