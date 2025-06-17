"""
TC -> O(rows*cols)
SC -> O(rows*cols)
Logic
Perform an iterative DFS (using a stack) to flood fill all connected cells
that have the same original color as the starting cell (sr, sc). It replaces each of
those cells with the new color. A visit set ensures no cell is processed more than once.
The search explores in 4 directions (up, down, left, right) until all reachable, same-colored cells are updated.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        visit = set()

        def dfs(row, col, target_color, curr_color):
            stack = [[row,col,curr_color]]
            visit.add((row,col))
            directions = [
                [-1,0],[1,0],
                [0,-1],[0,1]
            ]
            while stack:
                r,c,clr = stack.pop()
                image[r][c] = target_color
                for delrow, delcol in directions:
                    nrow, ncol = r+delrow, c+delcol
                    if 0<=nrow<ROWS and 0<=ncol<COLS and image[nrow][ncol]==clr and (nrow, ncol) not in visit:
                        stack.append([nrow,ncol, image[nrow][ncol]])
                        visit.add((nrow,ncol))
        dfs(sr, sc, color, image[sr][sc])
        return image