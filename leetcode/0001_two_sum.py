class Solution:
    def twoSum(self, nums: list[int], target: int):
        freq = {}

        for i, key in enumerate(nums):
            counter_pair = target - key
            if counter_pair in freq:
                return [freq[counter_pair], i]
            freq[key] = i