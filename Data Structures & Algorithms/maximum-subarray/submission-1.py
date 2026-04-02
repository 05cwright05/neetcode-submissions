class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_answer = -9999999999999 # might need to be really big negative
        running_sum = 0
        for i in range(0, len(nums)):
            if running_sum < 0:
                running_sum = 0
            running_sum+= nums[i]
            best_answer = max(best_answer, running_sum)
        return best_answer