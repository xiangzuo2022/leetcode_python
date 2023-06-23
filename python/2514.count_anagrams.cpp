using LL = long long;
LL M = 1e9+7;
class Solution {
    LL inv[100005];
public:
    int countAnagrams(string s) 
    {
        vector<string>str_arr;
        istringstream in(s);
        int k = 0;
        for (string word; in>>word; k++) 
            str_arr.push_back(word);    
                
        inv[1] = 1;
        for(int i=2; i<=100000; ++i)
            inv[i]=(M-M/i) * inv[M%i] % M;
        
        LL ret = 1;
        for (auto& str: str_arr)
        {
            ret = ret * helper(str) % M;
        }
        return ret;
    }
    
    LL helper(string& s)
    {
        unordered_map<int,int>Map;
        for (auto ch: s)
            Map[ch]+=1;
        
        int N = s.size();
        LL ret = 1;
        for (int i=1; i<=N; i++)
            ret = ret * i % M;
        
        for (auto [k,v]:Map)
        {
            for (int i=1; i<=v; i++)
                ret = ret * inv[i] % M;
        }
        return ret;
    }
};

https://www.youtube.com/watch?v=J0GqEtGZULE&list=PLwdV8xC1EWHrtgsYCcDTXIMVaHSlsnLzL

2514.Count-Anagrams
本题的本质就是计算每个单词的distinct permutation的乘积。

对于一个单词长度为n，则distinct permutation的数目就是n! / prod{k_i !}，其中k_i就是每个字母在该单词中出现的频次。

本题的难点在于模下计算。上述公式中ki的阶乘是在分母上，所以需要取逆元。即转换为 n! * prod{inv[k_i]!}。因为ki的频次不超过1e5，所以我们可以提前预处理，用线性时间算出1e5以内所有的inv[i].