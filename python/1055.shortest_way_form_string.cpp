/* 状态机解法 O(n)*/
class Solution {
public:
    int shortestWay(string source, string target) {
        int m = source.size();
        source = "#" + source;
        
        int next[m+1][26];
        for(int ch=0; ch<26; ch++)
            next[m][ch] = -1;
        
        for(int i= m-1; i >=0; i--){
            for(int ch=0; ch< 26; ch++)
                next[i][ch] = next[i+1][ch];
            next[i][source[i+1]-'a'] = i+1;
        }
            
        int j = 0; 
        int count = 1;
        for(int i=0 ; i < target.size(); i++){
            if(next[j][target[i]-'a']!=-1)
                j = next[j][target[i]-'a'];
            else{
                if(j == 0) return -1;
                j = 0;
                count ++;
                i--;
            }
        }
        return count;
    }
};


// 0  123456
//    aXbXXcX           [ab]bc
 
// next[0]['a'] = 1
// next[1]['b'] = 3
// next[3]['b'] = -1
    
// next[0]['b'] = 3
// next[3]['c'] = 5
    
// next[i][ch] = j

// 26m