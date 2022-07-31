/* binary search n*log(m)*k */
https://www.youtube.com/watch?v=2eDAImbp8C4

class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        vector<vector<int>> pos(26);
        for (int i=0; i< s.size(); i++)
            pos[s[i]-'a'].push_back(i);            
        
        int count = 0;
        for (auto word: words){
            if (word.size() > s.size())
                continue;
            if(check(word, pos))
                count ++;
        }
        return count;
    }
    
    bool check(string &word, vector<vector<int>>&pos){
        int i = 0;
        for(auto ch: word){
            auto iter = lower_bound(pos[ch-'a'].begin(), pos[ch-'a'].end(), i);
            if(iter == pos[ch-'a'].end())
                return false;
            i = *iter + 1;
        }
        return true;        
    }
};


// S = X X a b a X a X
//         ^
// pos[a] = {3, 5, 7}
// pos[b] = {2, 4, 8}
// pos[c] = {1, 6 ....}

// word = a b c 
//          ^
         
// double pointers (n+m)*k
// binary search n*log(m)*k

/* solution 2:状态机 O(n * k)*/

class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int m = s.size();
        s = "#" + s; //s[1:m]
        int next[m+1][26];
        int ret = 0;
        for (int k=0; k< 26; k++){
             next[m][k] = -1;
         }
        for (int i=m; i>=1;i--){
            for (int k=0; k< 26; k++)
                next[i-1][k] = next[i][k];
            next[i-1][s[i]-'a'] = i;            
        }
        
        for(auto word: words){
            int i = 0; 
            int flag = 1;
            for(auto ch:word){
                i = next[i][ch-'a'];
                if (i == -1) {
                    flag = 0;
                    break;
                }
            }
            if(flag) ret ++;            
        }
        return ret;
        
    }
    
    
};

//    0 1 2 3 4 5 6 7 8 9 10
// S =  X X a b a X a c X b
//    ^
// array size = m * 26; m = S.size()
       
// next[10][a] = -1
// next[10][b] = -1
// next[10][c] = -1
// next[10][d] = -1
    
// next[9][a] = -1
// next[9][b] = 10
// next[9][c] = -1
// next[9][d] = -1

// ....
    
// next[0][a] = 3
// next[3][b] = 4
// next[4][c] = 8
// next[8][d] = -1
    

// word = a b c 
//          ^
         
