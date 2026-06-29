class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns=""
        for i in s:
            if i!="i":
                ns=ns+i
            else:
                ns=ns[::-1]
        return ns