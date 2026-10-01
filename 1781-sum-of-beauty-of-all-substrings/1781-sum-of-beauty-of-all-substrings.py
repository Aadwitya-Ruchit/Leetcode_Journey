class Solution:
    def maxCount(self, freq):
        max_count = 0
        for count in freq:
            max_count = max(max_count, count)
        return max_count

    def minCount(self, freq):
        min_count = float('inf')
        for count in freq:
            if count != 0:
                min_count = min(min_count, count)
        return min_count

    
    def beautySum(self, s: str) -> int:
        sum_beauty = 0
        n = len(s)
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                beauty = self.maxCount(freq) - self.minCount(freq)
                sum_beauty += beauty
        return sum_beauty


            