class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n=len(nums); res=0
        for i in range(n):
            j=i; imbalance=0; _set=set()
            while j<n:
                if nums[j] not in _set and nums[j]-1 in _set and nums[j]+1 in _set:
                    imbalance-=1
                if j-i>0 and nums[j] not in _set and nums[j]-1 not in _set and nums[j]+1 not in _set:
                    imbalance+=1
                _set.add(nums[j])
                res+=imbalance
                j+=1
        return res