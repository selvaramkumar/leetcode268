class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        # ans = expected_sum - actual_sum
        return n*(n+1)//2 - sum(nums)
s=Solution()
arr=[0,1]
print(s.missingNumber(arr))     
