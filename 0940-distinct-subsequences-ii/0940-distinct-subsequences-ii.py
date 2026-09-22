class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = {}
        
        for char in s:
            total = (1 + sum(dp.values())) % MOD
            dp[char] = total
            
        return sum(dp.values()) % MOD