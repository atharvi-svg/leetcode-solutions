class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer=[]

        def helper(index, current):

            #base case-
            if index == len(nums):
                answer.append(current[:])
                return 
            #recursive function 
            #choice 1 take-
            current.append(nums[index])
            
            helper(index+1 , current)
           
            #choice 2 not take-
            current.remove(nums[index])
            
            helper(index+1,current)

            
        helper(0,[])

        return answer





        