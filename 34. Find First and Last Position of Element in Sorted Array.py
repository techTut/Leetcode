class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findElement(nums, target, True)
        if first == -1:
            return [-1, -1]
        return [first, self.findElement(nums, target, False)]
    
    def findElement(self, nums, target, first):
        left = 0
        right = len(nums)-1
        idx = -1
        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] == target:
                idx = mid
                if first:
                    right = mid -1
                else:
                    left = mid +1
            elif target< nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        return idx
    