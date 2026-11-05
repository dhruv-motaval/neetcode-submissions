class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,x in enumerate(nums):
            y = target - x

            if y in hashmap:
                return [hashmap[y],i]
            
            hashmap[x] = i