class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_answer = -99999999999
        for i in range(0, len(nums)):
            current_answer = 0;
            for z in range(i, len(nums)):
                current_answer+=nums[z]
                best_answer = max(best_answer, current_answer)
        return best_answer