class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            indexA = i
            numA = nums[i]
            for j in range((i + 1), len(nums)):
                indexB = j
                numB = nums[j]
                if ((numA + numB)== target):
                    return [indexA,indexB]