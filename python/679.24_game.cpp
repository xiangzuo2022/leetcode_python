class Solution {
public:
    bool judgePoint24(vector<int>& cards) 
    {
        vector<double>nums(4);
        for(int i=0;i<4;i++)
            nums[i] = double(cards[i]);
        sort(nums.begin(), nums.end());
        while(1){
            // compute 24 for nums
            unordered_set<double>rets = helper(nums, 0, 3);
            for(auto x:rets){
                if(abs(x - 24.0) < 1e-10)
                    return true;
            }           
            
            if(next_permutation(nums.begin(), nums.end())==false)
                break;
        }
        return false;
    }
    
     unordered_set<double>helper(vector<double>&nums, int a, int b){
        if(a==b)return {nums[a]};
        unordered_set<double>rets;
        for(int i =a;i < b;i ++){
            unordered_set<double> A = helper(nums, a, i);
            unordered_set<double> B = helper(nums, i+1, b);
            for(double x: A)
                for(double y:B){
                    rets.insert(x+y);
                    rets.insert(x-y);
                    rets.insert(x*y);
                    if(y!=0)
                        rets.insert(x/y);
                }
            
        }
         return rets;
     }
};

https://www.youtube.com/watch?v=7zlzniZ5xWs