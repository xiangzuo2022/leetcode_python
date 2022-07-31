class MyCalendar {
    map<int, int>Map;
public:
    MyCalendar() {
        
    }
    
    bool book(int start, int end) {
        auto iter1 = Map.upper_bound(start);
        if(iter1 != Map.begin()){
            auto iter2 = prev(iter1, 1);
            if(iter2->second > start)
                return false;
        }
        if(iter1 != Map.end() && iter1->first < end){
            return false;
            
        }
        Map[start] = end;
        return true;
        
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */ 

// 0-----5
//        6 ----7 
//                 9-------12

// start ------- end 
https://www.youtube.com/watch?v=g30lRE3ASiA
此题是训练C++里使用有序容器数据结构（比如说map，set等）基本功的一道题。

首先，使用Map.upper_bound(start)找到第一个大于start的迭代器iter，检查其对应的区间[a,b)是否与[start,end)重合。记得前提是iter有意义，也就是iter!=Map.end().

接着，将iter回退一个位置，找到第一个小于等于start的迭代器，检查其对应的区间[a,b)是否与[start,end)重合。同样，记得前提是此时的iter有意义，也就是iter!=Map.begin().