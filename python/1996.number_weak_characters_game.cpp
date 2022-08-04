class Solution {
    static bool cmp(vector<int>&a, vector<int>&b){
        if(a[0] != b[0])
            return a[0] < b[0];
        else
            return a[1] > b[1];
    }
public:
    int numberOfWeakCharacters(vector<vector<int>>& properties) 
    {
        sort(properties.begin(), properties.end(), cmp);
        stack<int>Stack;
        int ret = 0;
        for (int i = 0; i < properties.size(); i++){
            while(!Stack.empty() && Stack.top() < properties[i][1]){
                Stack.pop();
                ret++;
            }
            Stack.push(properties[i][1]);
        }
        return ret;
    }
};
https://www.youtube.com/watch?v=XSxnbDFz_2U&t=313s
attack: [1 2 3 4 4 5 6 7 8]
defense:[3 5 3 3 2 1 3 4 7]