class ProcSqrt():
    def sqrtnum(self, x):
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        while start <= end:
            mid = (start + end) / 2
            if abs(mid - x / mid) <= 1e-06:
                return mid
            elif mid > x / mid:
                end = mid
            elif mid < x / mid:
                start = mid
        return mid


n = 2
print(ProcSqrt().sqrtnum(n))
