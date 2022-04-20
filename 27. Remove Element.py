class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertPosition = 0
        for num in nums:
            if num != val:
                nums[insertPosition] = num
                insertPosition += 1
        return insertPosition
    