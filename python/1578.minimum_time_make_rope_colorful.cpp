
class Solution {
public:
    int minCost(string s, vector<int>& cost) 
    {
        int ret = 0;
        for (int i=0; i<s.size();)
        {
            int j=i;
            int maxValue = 0;
            int sum = 0;
            while (j<s.size() && s[j]==s[i])
            {
                sum += cost[j];
                maxValue = max(maxValue, cost[j]);
                j++;
            }
            ret += sum - maxValue;
            i = j;
        }
        return ret;

    }
};

// XX[X]XX
// ret += sum - maxValue
https://www.youtube.com/watch?v=n6fUMuVS-X8