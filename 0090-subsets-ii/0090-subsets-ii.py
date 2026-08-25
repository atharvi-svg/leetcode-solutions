class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []

        def helperfn(n, current):

            # Base case
            if len(nums) == n:
                result.append(current[:])
                return

            # Recursive case

            # Pick
            current.append(nums[n])
            helperfn(n + 1, current)
            current.pop()

            # Skip duplicates
            while n + 1 < len(nums) and nums[n] == nums[n + 1]:
                n += 1

            # Don't pick
            helperfn(n + 1, current)

        helperfn(0, [])

        return result
            