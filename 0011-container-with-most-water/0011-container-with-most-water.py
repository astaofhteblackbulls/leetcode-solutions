class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea=0
        l=0
        r=len(height)-1
        while l<r:
            width=r-l
            h=min(height[l],height[r])
            area=h*width
            maxarea=max(maxarea,area)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return maxarea