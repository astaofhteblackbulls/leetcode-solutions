class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        arr=sorted(satisfaction,reverse=True)
        pre=0
        val=0
        for i in range(0,len(arr)):
            if arr[i]+pre>0:
                pre=pre+arr[i]
                val=val+pre
            else:
                continue
        return val


        