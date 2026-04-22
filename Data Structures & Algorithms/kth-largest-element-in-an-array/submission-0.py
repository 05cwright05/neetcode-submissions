class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        well the easy approach will be to srt the list and go thru to the kth starting from end


        """
        nums.sort()
        if k > len(nums):
            return -1

        return nums[len(nums)-k]
