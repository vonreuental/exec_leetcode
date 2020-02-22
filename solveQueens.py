class SovleQueens:
    def solveQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
        result = []
        DFS([], [], [])
        print(f"解法共{len(result)}种")
        for i, val in enumerate(result):
            print(f"解法{i + 1}")
            for num in val:
                print("□" * num + "Q" + "□" * (n - num - 1))
        return [["." * i + "Q" + "." * (n - i - 1)
                 for i in sol] for sol in result]


n = 8
print(SovleQueens().solveQueens(n))
