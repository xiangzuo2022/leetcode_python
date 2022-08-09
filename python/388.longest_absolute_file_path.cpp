class Solution {
public:
    int lengthLongestPath(string input) 
    {
        vector<string>files;
        for(int i=0; i < input.size(); i++)
        {
            int start = i;
            while(i < input.size() && input[i]!='\n')
                i++;
            files.push_back(input.substr(start, i-start));
        }
        vector<string>dir;
        int result = 0; 
        
        for(string str:files){
            int k=0;
            while(k < str.size() && str[k]== '\t')
                k++; // number of tab
            if(dir.size() <= k)
                dir.resize(k+1);
            dir[k] = str.substr(k);            
            
            if(dir[k].find(".") != -1){ // it is a file not a directory
                int count = 0;
                for(int i=0; i<=k; i++)
                    count+= dir[i].size();
                count+=k;
                result = max(result, count);
            }
        }
        return result;
    }
};
https://www.youtube.com/watch?v=iDXMuU_eOsA&list=PLwdV8xC1EWHrtgsYCcDTXIMVaHSlsnLzL&index=976