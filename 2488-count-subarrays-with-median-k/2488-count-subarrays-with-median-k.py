class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        arr = []
        for n in nums:
            if n < k:
                arr.append(-1)
            elif n > k:
                arr.append(1)
            else:
                arr.append(0)
        
        book_pre = Counter()
        book_pre[0] = 1
        agg = 0
        check = False
        ans = 0
        for a in arr:
            if a == 0:
                check = True
            agg += a
            if check:
                ans += book_pre[agg] + book_pre[agg-1]
            else:
                book_pre[agg] += 1
        return ans