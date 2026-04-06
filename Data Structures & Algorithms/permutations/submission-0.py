class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #right now it allows choosing ourself multiple times so we might need to pass in a remaining nums

        result = []
        valid = [True for num in nums]

        def backtrack(path, valid):

            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if valid[i]:
                    path.append(nums[i])
                    valid[i] = False
                    backtrack(path, valid)
                    path.pop()
                    valid[i] = True

        backtrack([],valid)

        return result