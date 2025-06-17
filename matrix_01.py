"""
TC -> O(rows*cols)
SC ->O(row*cols)
Logic:
Use BFS algorithm.
1. create a result array with -1 values
2. Traverse through input array and insert the (row,col) of 0's to the queue and change the res[row][col] to 0.
In this logic, we start from 0 values and do BFS until we find -1
Now till the queue is empty, we check the 4 directions and update the res matrix if there is a -1
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])
        res = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    queue.append((r, c))

        neighbors = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]

        while queue:
            r, c = queue.popleft()
            for delrow, delcol in neighbors:
                nrow, ncol = r + delrow, c + delcol
                if 0 <= nrow < ROWS and 0 <= ncol < COLS and res[nrow][ncol] == -1:
                    res[nrow][ncol] = res[r][c] + 1
                    queue.append((nrow, ncol))

        return res
