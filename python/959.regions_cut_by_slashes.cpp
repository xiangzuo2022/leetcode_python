class Solution {
 int count, n;
   vector<int> f;
   public:
    int regionsBySlashes(vector<string>& grid) {
        n = grid.size();
        count = n * n * 4;//total number of polygons
        for (int i = 0; i < n * n * 4; ++i)
            f.push_back(i);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i > 0) uni(g(i - 1, j, 2), g(i, j, 0));
                if (j > 0) uni(g(i , j - 1, 1), g(i , j, 3));
                if (grid[i][j] != '/') {
                    uni(g(i , j, 0), g(i , j,  1));
                    uni(g(i , j, 2), g(i , j,  3));
                }
                if (grid[i][j] != '\\') {
                    uni(g(i , j, 0), g(i , j,  3));
                    uni(g(i , j, 2), g(i , j,  1));
                }
            }
        }
        return count;
    }

    int find(int x) {
        if (x != f[x]) {
            f[x] = find(f[x]);
        }
        return f[x];
    }
    void uni(int x, int y) {
        x = find(x); y = find(y);
        if (x != y) {
            f[x] = y;
            count--;
        }
    }
    int g(int i, int j, int k) {  //find the corresponding position for current triangle. Thinks this 1D array as a 2D array and each element is an array of size 4.
        return (i * n + j) * 4 + k;
    }
};

https://www.youtube.com/watch?v=46wmnzVyTv0