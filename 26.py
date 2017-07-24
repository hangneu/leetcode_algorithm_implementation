class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] == nums[read-1]:
                continue
            else:
                nums[write] = nums[read]
                write += 1
        return write
