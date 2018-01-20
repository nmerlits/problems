class Solution:
    def rec_search(self, i, j, nums, target):
        if i == j:
            return i if target <= nums[i] else i+1

        ind = (i + j) // 2
        if target == nums[ind]:
            return ind

        if target > nums[ind] and target < nums[ind+1]:
            return ind+1
        if target < nums[ind] and target > nums[ind-1]:
            return ind

        if target > nums[ind]:
            return self.rec_search(ind+1, j, nums, target)
        else:
            return self.rec_search(i, ind, nums, target)
        
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        return self.rec_search(0, len(nums)-1, nums, target)
