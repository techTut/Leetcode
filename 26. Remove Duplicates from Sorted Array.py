class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIdx = 1
        for num in nums:
            if num != nums[insertIdx-1]:
                nums[insertIdx] = num
                insertIdx +=1
        return insertIdx