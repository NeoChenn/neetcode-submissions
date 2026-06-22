class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        #base case: total == target and total > target
        #choices: include/exclude each value
        #constraints: sort candidates. if skip, skip duplicates aswell
        #backtrack step: pop

        #[1, 2, 2, 4, 5, 6, 9] 
        #[[1, 2, 5], ]
       
        res = []
        cur = []
        candidates.sort()
        def bt_dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            bt_dfs(i + 1, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            bt_dfs(i + 1, total)

        bt_dfs(0, 0)
        return res
        