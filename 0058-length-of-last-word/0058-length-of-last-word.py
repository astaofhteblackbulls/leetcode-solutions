class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip()
        i=len(s)-1
        lw=""
        while i>=0 and s[i]!=" ":
            lw=lw+s[i]
            i=i-1
        return len(lw)


        
        