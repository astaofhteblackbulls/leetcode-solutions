class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a=0
        b=0
        while b<len(nums):
            if nums[b]!=val:
                 nums[a]=nums[b]
                 a=a+1
            b=b+1
        return a