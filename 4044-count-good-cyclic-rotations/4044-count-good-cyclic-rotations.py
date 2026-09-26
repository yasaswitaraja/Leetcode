class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n//2
        total = sum(nums)
        l = sum(nums[:half])
        c=0
        for i in range(len(nums)):
            if l > total -l:
                c+=1
            l = l - nums[i] + nums[(i+ half)%n]
        return c    
                
            
        