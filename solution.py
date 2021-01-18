class Solution:
    def missingNumber(self, nums) -> int:
        expec_sum=(len(nums))*(len(nums)+1)//2
        actual=sum(nums)
        return abs(expec_sum-actual)
s=Solution()
arr=[0,1]
print(s.missingNumber(arr))     