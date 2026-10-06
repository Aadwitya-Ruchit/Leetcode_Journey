class Solution:
    def myPow(self, x, n):

        N = abs(n)
        ans = 1

        while N > 0:

            if N & 1:
                ans *= x

            x *= x
            N >>= 1

        return 1 / ans if n < 0 else ans