class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        cand=None
        n=len(nums)
        for i in nums:
            if count==0:
                cand=i
            if i==cand:
                count=count+1
            else:
                count=count-1
        return cand
        