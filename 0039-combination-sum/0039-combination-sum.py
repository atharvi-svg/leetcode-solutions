class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        def helperfn(n, current, target):

            # BASE CASE
            if target == 0:
                result.append(current[:])
                return

            if target < 0:
                return

            if n == len(candidates):
                return

            # PICK
            current.append(candidates[n])

            # We stay at n because we can reuse
            # the same candidate
            helperfn(n, current, target - candidates[n])

            # BACKTRACK
            current.pop()

            # NOT PICK
            helperfn(n + 1, current, target)

        helperfn(0, [], target)

        return result


