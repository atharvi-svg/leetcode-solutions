class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        
       

        def helperfn(open,close,current):
             if len(current)==2*n:
                result.append(current)
                return 
             if open<n:
                #we recurse , therefore we call the recursive function
                helperfn(open+1,close,current+"(")
             if close<open:
                helperfn(open,close+1,current+")")
        helperfn(0, 0, "")

            
        return result

            
        