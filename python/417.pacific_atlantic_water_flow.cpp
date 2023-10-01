class Solution {
    vector<pair<int, int>>dir;
    int M, N;
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        M = matrix.size();
        if(M==0)return {};
        N = matrix[0].size();
        
        auto Pac = vector<vector<int>>(M, vector<int>(N, 0));
        auto Atl = vector<vector<int>>(M, vector<int>(N, 0));
        // border cases
        for(int i=0; i< M; i++)
            dfs(i, 0, matrix, Pac);
        for(int j=0; j< N; j++)
            dfs(0, j, matrix, Pac);
        
        for(int i=0; i< M; i++)
            dfs(i, N-1, matrix, Atl);
        for(int j=0; j< N; j++)
            dfs(M-1, j, matrix, Atl);
        
        vector<vector<int>>results;
        for(int i=0; i< M; i++)
            for(int j=0; j<N;j++){
                if(Pac[i][j]==1 && Atl[i][j]==1)
                    results.push_back({i, j});
            }
        return results;
        
    }
    
    void dfs(int i, int j, vector<vector<int>>& matrix, vector<vector<int>>& Sea){
        Sea[i][j] = 1;
        dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for(int k=0; k<4;k++){
            int x = i+dir[k].first;
            int y = j+dir[k].second;
            if(x<0 || x==M || y<0 || y==N)
                continue;
            if(Sea[x][y] == 1)
                continue;
            if(matrix[x][y]<matrix[i][j])
                continue;
            dfs(x, y, matrix, Sea);
        }
        
    }
};

https://www.youtube.com/watch?v=N3EHz19C0G0&list=PLwdV8xC1EWHrtgsYCcDTXIMVaHSlsnLzL&index=979&t=351s

# https://www.youtube.com/watch?v=s-VkcjHqkGI
# DFS + visit
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        # pacific and altantic columns
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        # pacific and altantic rows
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
