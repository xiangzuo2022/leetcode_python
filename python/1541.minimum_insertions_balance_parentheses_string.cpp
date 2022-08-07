class Solution {
public:
    int minInsertions(string s) 
    {
        int count = 0;
        int ret = 0;
        for (int i=0; i < s.size(); i++)
        {
            if(s[i] == '(')
                count++;
            else{
                if(i+1 <s.size() && s[i+1]==')')
                {
                    count--;
                    i++;
                }
                else
                {
                    ret++;
                    count--;
                }
            }
            if(count < 0){
                ret++;
                count=0;
            }
        }
        ret += count*2;
        return ret;
    }
};

// stack: ()
// greedy: count -> unmatched left parethesis
//         count ++
// 1. must two consecutive ) cancel one (;
// 2. at the end, ret += count *2
https://www.youtube.com/watch?v=U1nwBAIQ-oc