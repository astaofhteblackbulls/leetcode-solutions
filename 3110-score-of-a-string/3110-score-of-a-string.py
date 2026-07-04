class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=[]
        sum=0
        for i in s:
            arr.append(i)
        for i in range(0,len(arr)-1):
            sum=sum+abs(ord(arr[i])-ord(arr[i+1]))
        return sum
