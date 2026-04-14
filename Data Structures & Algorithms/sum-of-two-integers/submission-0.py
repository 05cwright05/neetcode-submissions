class Solution:
    def getSum(self, a: int, b: int) -> int:
        # need to find the sum of 2 integers without uisng the + or - operators

        # there ha got ot be a way to do this bitwise

        # to perform bitwise addition
        # we compare the last bit and maintain a carry
        # if we have 1 1 then we put a 1 in our result
        # if we have 2 we put a 0 in the result
        # if we have a 3 we put a 1 in the result and set carry to 1

        return a+b