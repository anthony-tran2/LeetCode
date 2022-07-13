class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_dif = -1
        lowest_num = nums[0]
        for x in range(1, len(nums)):
            if nums[x] < lowest_num:
                lowest_num = nums[x]
            elif nums[x] - lowest_num > max_dif:
                max_dif = nums[x] - lowest_num
        if max_dif <= 0:
            return -1
        return max_dif
    