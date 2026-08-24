class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def sumByD(div):
            total = 0

            for x in nums:
                total += math.ceil(x / div)

            return total

        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2

            if sumByD(mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low