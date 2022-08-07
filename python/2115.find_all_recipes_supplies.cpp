class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) 
    {
        
        unordered_map<string, vector<string>>next;
        unordered_map<string, int>indegree;
        for(int i=0; i< recipes.size(); i++){
            for(int j=0; j< ingredients[i].size(); j ++){
                next[ingredients[i][j]].push_back(recipes[i]);
                indegree[recipes[i]] += 1;
            }
        }
        
        unordered_set<string>wanted(recipes.begin(), recipes.end());
        queue<string>q;
        for(string s: supplies)
            q.push(s);
        vector<string>ret;
        while(!q.empty()){
            string cur = q.front();
            q.pop();
            if(wanted.find(cur)!=wanted.end())
                ret.push_back(cur);
            for(auto x:next[cur]){
                indegree[x]-= 1;
                if(indegree[x] == 0)
                    q.push(x);
            }
        }
        return ret;
    }
};