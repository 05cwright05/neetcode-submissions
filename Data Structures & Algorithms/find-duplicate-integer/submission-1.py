class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #need to do in constant space
        #brain destroyer i see the first number and go to that index in the array and mark as a -1 but before i do that
        # i grab its value and go do that to the next number, if i ever hit a -1 i return the index. 
        curr = nums[0]
        while True:
            temp = nums[curr]
            if temp == -1:
                return curr
            nums[curr] = -1
            curr = temp