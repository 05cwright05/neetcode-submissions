class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # could solve in O(n^2) if we just computed it by going down the list
        # but if we are clever we can do like a rolling thing where we go through it once, and then we divide by the curretn number
        # edge case being 0, in that case we are fucked because suppose i have
        # 0, 1, 2, then i would say the total product is 0 but if i divide by 0 it is still 0. Maybe in the case that it is a zero we go back through everything and recompute
        # though that would mean in the case of all zeroes then our time complexity would remain O(n^2)
        # or we could do this genius bruger

        total = 1
        # if we have more than one zero than the output will be all zeros
        num_zeroes = 0
        total_excluding_zero = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                total_excluding_zero *= nums[i]
            else:
                num_zeroes+=1
            total *= nums[i]
        output = []
        for num in nums:
            if num != 0:
                output.append(int(total / num))
            else:
                if num_zeroes == 1:
                    output.append(total_excluding_zero)
                else:
                    output.append(0)
        return output

