class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #To speed the jawn up we will sort first and then see if it ever matches its neighbor
        nums.sort()
        for i in range(0, len(nums) -1):
            if nums[i] == nums[i+1]:
                return True
        return False
