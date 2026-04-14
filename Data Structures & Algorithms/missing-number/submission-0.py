class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # since we have a predicatble range and know we are only missing one we can probbly use math
        # the sum of numbers in range of 1-n is n(n+1)/2)  i think
        # lets check say i have 1,2,3 = 

        expected_value = (len(nums) * (len(nums) + 1)) //  2

        for value in nums:
            expected_value -= value
        return expected_value