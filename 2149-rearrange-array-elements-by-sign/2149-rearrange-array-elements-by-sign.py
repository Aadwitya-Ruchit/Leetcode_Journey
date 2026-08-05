class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n

        posindex = 0
        negindex = 1

        for i in range(n):
            if nums[i] > 0:
                arr[posindex] = nums[i]
                posindex += 2
            else:
                arr[negindex] = nums[i]
                negindex += 2
        return arr