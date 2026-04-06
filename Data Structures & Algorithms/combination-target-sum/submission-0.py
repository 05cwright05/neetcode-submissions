class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(curr_solution, target, index):
            if target==0:
                result.append(curr_solution[:])
                return
            for i in range(index, len(nums)):
                if target - nums[i] >= 0:
                    curr_solution.append(nums[i])
                    backtrack(curr_solution, target-nums[i], i)
                    curr_solution.pop()
        backtrack([], target, 0)
        return result
