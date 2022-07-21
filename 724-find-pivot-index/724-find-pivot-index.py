class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum1 = 0
        sum2 = sum(nums[1:])
        
        for i in range(len(nums)):
            if sum1 == sum2:
                return i
            sum1 += nums[i]
            if i + 1 == len(nums):
                return -1
            sum2 -= nums[i + 1]