class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
            j = j + 1

        return i