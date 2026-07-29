class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        def solve(arr):
            n=len(arr)
            if n == 0:
                return 0
            if n==1:
                return arr[0]

            dp= [0]*(n+1)
            dp[1]= arr[0]

            for i in range(2,n+1):
                dp[i]= max(arr[i-1]+dp[i-2], dp[i-1])
            return dp[n]
        
        return max(solve(nums[:len(nums)-1]), solve(nums[1:]))
