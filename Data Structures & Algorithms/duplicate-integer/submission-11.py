class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sort = sorted(nums)
        i = 0
        while i < len(nums_sort) - 1:
            if nums_sort[i] == nums_sort[i + 1]:
                return True
            i = i + 1
        return False
