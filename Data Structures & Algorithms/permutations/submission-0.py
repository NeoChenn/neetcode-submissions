class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case: length of permutation == length of nums
        #choices: each num in nums
        #constraints: no repeats

        res = []
        perm = []

        def bt_dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in nums:
                if n in perm:
                    continue
                perm.append(n)
                bt_dfs()
                perm.pop()

        bt_dfs()
        return res
