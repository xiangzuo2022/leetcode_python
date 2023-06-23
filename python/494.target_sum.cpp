// solution 1 DFS 

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) 
    
    {
        const int sum = std::accumulate(nums.begin(), nums.end(), 0);
        if(sum < std::abs(target)) return 0;
        int ans =0;
        dfs(nums, 0, target, ans);
        return ans;
    }
    void dfs(vector<int>& nums, int d, int target, int &ans)
    {
        if(d == nums.size())
        {
            if(target == 0)
                ans++;
            return;
        }
        dfs(nums, d+1, target - nums[d], ans);
        dfs(nums, d+1, target + nums[d], ans);
    }
};
https://www.youtube.com/watch?v=r6Wz4W1TbuI