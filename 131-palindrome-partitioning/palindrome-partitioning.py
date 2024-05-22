class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = True if j - i <= 2 else dp[i + 1][j - 1]
        
        @functools.lru_cache()
        def dfs(start_idx):
            if start_idx == len(s):
                return [[]]
            res = []
            for end_idx in range(start_idx, len(s)):
                if dp[start_idx][end_idx]:
                    res.extend([s[start_idx:end_idx+1]] + comb for comb in dfs(end_idx + 1))
            return res
        
        return dfs(0)