class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        L, ans = len(nums), list([[]])

        mask = 2**L - 1
        while mask:
            copy, i, subset = mask, L - 1, list()
            while copy:
                if copy & 1: subset.append(nums[i])
                i, copy = i - 1, copy >> 1

            ans.append(subset)
            mask -= 1

        return ans