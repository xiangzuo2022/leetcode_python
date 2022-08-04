// zero is the speical case 

class ProductOfNumbers {
    vector<int>pre;
    int n = 0;
    int lastZero;
public:
    ProductOfNumbers() {
        n = 0;
        lastZero = 0;
        pre.push_back(1);
    }
    
    void add(int num) {
        n++;
        if(num == 0){
            pre.push_back(1);
            lastZero = n;
        }
        else{
            pre.push_back(pre.back()* num);
        }
        
        
    }
    
    int getProduct(int k) {
        if(lastZero <= n-k){
            return pre[n] / pre[n-k];
        }
        else
            return 0;
        
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */

// pre[i]: the product of nums[1]*nums[2]*...*nums[i]

// pre[i:j] = pre[j] / pre[i-1]
// 1 2 [3 2 4] = pre[4] / pre[1] = 48/2=24
// define pre[0] = 1

https://www.youtube.com/watch?v=CnEPfZYoCd8