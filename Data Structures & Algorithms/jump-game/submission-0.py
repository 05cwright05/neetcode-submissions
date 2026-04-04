class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #general strat is to take a value then
        #each step forward reduce it by one 
        # can choose to take new value if it is advantageous.
        # if we ever are at a value of -1 then it is not valid
        current_value = 0
        for i in range(0, len(nums)-1):
            current_value = max(current_value, nums[i])
            current_value-=1
            if current_value < 0:
                return False
        return True
        