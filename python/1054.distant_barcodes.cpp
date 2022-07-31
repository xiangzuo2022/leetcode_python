/* solution 1: priority queue, each time pick up the largest two elements from the queue 
*  将所有元素按照频次从大到小排列（所以相同的元素都会排在一起）。然后将这些元素先顺次填满答案序列index为奇数的位置，
*  然后在顺次填满答案序列index为偶数的位置。这样就能尽可能地保证相同的元素不会排在一起了。*  
*/
class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        unordered_map<int, int>Map;
        for(auto x:barcodes)
            Map[x] += 1;
        priority_queue<pair<int, int>>pq; // {freq, num}
        for(auto x : Map)
            pq.push({x.second, x.first});
        
        vector<int>ret;
        while(!pq.empty()){
            if(pq.size() == 1 && pq.top().first > 1)
                return{};
            int len = pq.size();
            vector<pair<int, int>>temp;
            for (int i=0; i<min(2, len); i++){
                ret.push_back(pq.top().second);
                if(pq.top().first > 1)
                    temp.push_back(pq.top());
                pq.pop();               
            }
            for(auto x:temp){
                x.first -= 1;
                pq.push(x);
            }
        }
        return ret;
        
    }
};

/* solution 2: insert
*  套路题：将所有数字按照频次放在一个优先队列里。每次从队列首取出两种不同的数字。频次减一之后再放回。
*/
class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        unordered_map<int, int>Map;
        for(auto x:barcodes)
            Map[x] += 1;
        vector<pair<int, int>>p;
        for(auto x : barcodes)
            p.push_back({Map[x], x}); // {freq, num}
        sort(p.begin(), p.end());
        reverse(p.begin(), p.end());
        
        vector<int>ret(barcodes.size());
        int i = 0;
        for(auto x: p){
            cout<<x.first<<","<<x.second<<", i= "<<i<<endl;
            ret[i] = x.second;
            i+=2;
            if(i >= barcodes.size())
                i = 1;
        }
        return ret;
        
    }
};


// P: 333333222111
// ret: 323232313131