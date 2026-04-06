class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def recHelper(curr_set, index_considering):
            if index_considering >= len(nums):
                output.append(curr_set[:])
                return
            curr_set.append(nums[index_considering])
            recHelper(curr_set, index_considering+1)
            curr_set.pop()
            recHelper(curr_set, index_considering + 1)
        
        recHelper([], 0)
        return output