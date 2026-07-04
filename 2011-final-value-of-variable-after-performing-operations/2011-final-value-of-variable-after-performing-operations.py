class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for i in range(0,len(operations)):
            if operations[i]=="++X":
                x=x+1
            elif operations[i]=="X++":
                x=x+1
            else: #operations[i]=='--X'or'X--':
                x=x-1
            print(x)
        return x
        