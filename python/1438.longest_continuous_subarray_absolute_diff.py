"""
sliding window
a video: https://www.youtube.com/watch?v=XiBfswQeQmU
关键是右端点不用清零， 因为求longest O(NlogN)
O(N)的解法关键是deque
"""

class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        multiset<int>Set({nums[0]});
        deque<int>qmax({0});
        deque<int>qmin({0});
        int mx = nums[0], mn = nums[0];
        int j = 0;
        int ret = 0;
        for (int i=0; i < nums.size(); i++){
            while(mx - mn <= limit){
                ret = max(ret, j-i+1);
                j++;
                if(j == nums.size()) break;
                // add nums[j] into qmax and qmin
                // get updated mx and mn
              
                while(qmax.size() > 0 && nums[j] >= nums[qmax.back()])
                    qmax.pop_back();
                qmax.push_back(j);
                mx = nums[qmax.front()];
                
                    
                while(qmin.size() > 0 && nums[j] <= nums[qmin.back()])
                    qmin.pop_back();
                qmin.push_back(j);
                mn = nums[qmin.front()];                    
            }
            
          
            if(j == nums.size()) break;
            if(qmax.size() > 0 && qmax.front() == i){
                qmax.pop_front();
                mx = nums[qmax.front()];
            }
            if(qmin.size() > 0 && qmin.front() == i){
                qmin.pop_front();
                mn = nums[qmin.front()];
            }
        }
        return ret;
    }
};