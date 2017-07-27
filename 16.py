class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l<r:
                total = sum([nums[i], nums[l], nums[r]])
                if abs(total-target) < abs(res - target):
                    res = total
                if total < target:
                    l += 1
                elif total > target:
                     r -= 1
                else:
                     return res
        return res
