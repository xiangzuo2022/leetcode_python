class Solution {
public:
    int nextGreaterElement(int n) {
        if(n==0) return -1;
         vector<int>digits;
        while (n>0){
            digits.push_back(n%10);
            n = n/10;
        }
        int i= 1;
        while(i<digits.size() && digits[i] >= digits[i-1]){
            i++;            
        }
        if(i==digits.size())
            return -1;
        int j = 0;
        while(j < digits.size() && digits[j]<=digits[i]){
            j++;
        }
        swap(digits[i], digits[j]);
        sort(digits.begin(), digits.begin()+i);
        reverse(digits.begin(), digits.begin()+i);
        long result = 0;
        for(int i=digits.size()-1; i >=0; i--){
            result *= 10;
            result += digits[i];            
        }
        if(result> INT_MAX)return -1;
        return result;
    }
};

https://www.youtube.com/watch?v=OKNpknDO86U