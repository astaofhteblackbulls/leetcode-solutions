class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=1
        a=0
        while b<len(nums):
            if nums[a]!=nums[b]:
                a=a+1
                nums[a]=nums[b]
            b=b+1
        return a+1