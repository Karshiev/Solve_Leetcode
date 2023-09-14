class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for idx1, el in enumerate(nums):
            idx2 = idx1
            for el2 in nums[idx1+1:]:
                idx2 += 1
                if el + el2 == target:
                    result.append(idx1)
                    result.append(idx2)
        return result