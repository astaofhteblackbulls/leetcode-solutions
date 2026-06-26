class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lb=0
        ub=len(nums)-1
        fst=-1
        ans=-1
        while lb<=ub:
            mid=(lb+ub)//2
            if nums[mid]==target:
                fst=mid
                ub=mid-1
            elif nums[mid]>target:
                ub=mid-1
            else:
                lb=mid+1
        lb=0
        ub=len(nums)-1
        while lb<=ub:
            mid=(lb+ub)//2
            if nums[mid]==target:
                ans=mid
                lb=mid+1
            elif nums[mid]>target:
                ub=mid-1
            else:
                lb=mid+1
        return [fst,ans]

