class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if i != sorted_nums[i]:
                return i
        return len(nums)