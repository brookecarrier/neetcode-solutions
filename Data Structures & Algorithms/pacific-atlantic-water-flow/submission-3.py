class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # for all pacific border cells do dfs, store in bool list
        # same for atlantic
        # valid if cell higher or equal
        # return where both lists are true
        def dfs(r, c, lst):
            if lst[r][c]:
                return

            lst[r][c] = True
            val = heights[r][c]

            # check left
            if (c-1) >= 0 and heights[r][c-1] >= val:
                dfs(r, c-1, lst)
            # check right
            if (c+1) < cols and heights[r][c+1] >= val:
                dfs(r, c+1, lst)
            # check top
            if (r-1) >= 0 and heights[r-1][c] >= val:
                dfs(r-1, c, lst)
            # check bottom
            if (r+1) < rows and heights[r+1][c] >= val:
                dfs(r+1, c, lst)
            
            heights[r][c] = val
            
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic = [[False for _ in range(cols)] for _ in range(rows)]

        # pacific top row
        for c in range(cols):
            dfs(0, c, pacific)
        # pacific left cols
        for r in range(rows):
            dfs(r, 0, pacific)
        # atlantic bottom row
        for c in range(cols):
            dfs(rows-1, c, atlantic)
        # atlantic right row
        for r in range(rows):
            dfs(r, cols-1, atlantic)
        
        output = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    output.append([r, c])
        
        return output


        



        
     