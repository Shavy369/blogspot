def longestIncreasingPath(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    cache = [[0]*cols for _ in range(rows)]

    def dfs(r, c):
        if cache[r][c]:
            return cache[r][c]
        val = matrix[r][c]
        best = 1
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > val:
                best = max(best, 1 + dfs(nr, nc))
        cache[r][c] = best
        return best

    return max(dfs(r, c) for r in range(rows) for c in range(cols))

# Example
print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # Output: 4
