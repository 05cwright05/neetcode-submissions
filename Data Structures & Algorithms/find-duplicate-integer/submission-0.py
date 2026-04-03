class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # apprach one would to be to use dictionary with the value and how nany times it has been used
        count_dict = {}
        for num in nums:
            if count_dict.get(num):
                return num
            else:
                count_dict[num] = 1
                