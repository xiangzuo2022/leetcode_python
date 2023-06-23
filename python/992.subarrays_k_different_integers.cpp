class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) 
    {
        return atMostK(nums, k) - atMostK(nums, k-1);
    }
    
    int atMostK(vector<int>& nums, int k)
    {
        unordered_map<int, int>Map;
        int count = 0;
        int i=0;
        
        for(int j=0; j<nums.size(); j++)
        {
            Map[nums[j]]++;
            while(Map.size()>k)
            {
                Map[nums[i]]--;
                if(Map[nums[i]]==0)
                    Map.erase(nums[i]);
                i++;
            }
            count += j-i+1;
        }
        return count;
    }
};

https://www.youtube.com/watch?v=5Ec68Qr2GTM