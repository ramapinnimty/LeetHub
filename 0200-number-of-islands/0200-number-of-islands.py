class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: Check if the grid is None
        if not grid:
            return 0

        def bfs(r, c):
            q = collections.deque() # create a queue for BFS
            q.append((r, c)) # add the current cell to the queue

            # Chain the islands while the queue is not empty
            while q:
                r, c = q.popleft() # unpack the row & col values
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    if (r+dr) in range(rows) \
                        and (c+dc) in range(cols) \
                        and grid[r+dr][c+dc] == '1' \
                        and (r+dr, c+dc) not in visited:
                        q.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        # Iterate through every cell starting from the top-left
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    visited.add((row, col)) # add the current cell to the visited set
                    bfs(row, col)
                    # Increment with the newly found island
                    islands += 1

        return islands