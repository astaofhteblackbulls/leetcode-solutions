class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a=0
        b=len(nums)-1
        while a<=b:
            avg=(a+b)//2
            if target==nums[avg]:
                return avg
            if target<nums[avg]:
                b=avg-1
            if target>nums[avg]:
                a=avg+1
        return a
