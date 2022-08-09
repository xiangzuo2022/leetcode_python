class Solution {
public:
    vector<int> findAnagrams(string s, string p) 
    {
        vector<int>P(255, 0); //P[i]: ASCII - i
        for(auto x:p)
            P[x]++;
        vector<int>S(255, 0);
        vector<int>result;
        
        for(int i=0;i<s.size(); i++){
            S[s[i]]++;
            if(i>=p.size())
                S[s[i-p.size()]]--;
            if(S ==P)
                result.push_back(i-p.size()+1);
                
        }
        return result;
            
    }
};
 // one pointer and window size is known
https://www.youtube.com/watch?v=I9xCo3UVomE&list=PLwdV8xC1EWHrtgsYCcDTXIMVaHSlsnLzL&index=978