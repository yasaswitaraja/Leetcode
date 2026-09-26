class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        
        # Helper function to count the cumulative number of '1' bits up to num
        def cnt1(num: int) -> int:
            res = 0
            for i in range(num.bit_length()):
                cur = num % (1 << (i + 1))
                res += (num - cur) // 2 
                if cur >= 1 << i:
                    res += cur + 1 - (1 << i)
            return res
        
        # Helper function to count the cumulative weighted number of '0' bits up to num
        def acc0(num: int) -> int:
            res = 0
            for i in range(num.bit_length()):
                cur = num % (1 << (i + 1))
                res += (num - cur) // 2 * i
                if cur >= 1 << i:
                    res += (cur + 1 - (1 << i)) * i
            return res
        
        # Function to calculate the bit count for a given boundary
        def count(bound: int) -> int:
            # Find the target number where bound is located
            target = bisect_left(range(bound), bound, key=cnt1)
            rest = bound - cnt1(target - 1)
            cnt = acc0(target - 1)
            
            # Adjust the count based on remaining bits
            for i in range(target.bit_length()):
                if target & (1 << i):
                    cnt += i
                    rest -= 1
                    if not rest:
                        break
            return cnt
        
        # Process each query and compute the product of elements in the given range
        return [pow(2, count(high + 1) - count(low), mod) for low, high, mod in queries]