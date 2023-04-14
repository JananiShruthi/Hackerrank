class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for index, val in enumerate(nums):
            b = target - val
            if(b in d):
                return [d[b], index]
            else:
                d[val] = index
