// two pointers
class Solution {
public:
	int compress(vector<char>& chars) {
		if(chars.size() < 2)
			return chars.size();

		int  i = 0;
		int  j = 0;

		while(i < chars.size()) {
			chars[j] = chars[i];
			int cnt = 0;
			while(i < chars.size() && chars[i] == chars[j]) {
				cnt++;
				i++;
			}

			if(cnt == 1) {
				j++;
			} else {
				string str = to_string(cnt);
				for(auto ch: str)
					chars[++j] = ch;
				j++;
			}
		}

		return j;
	}
};

https://www.youtube.com/watch?v=IhJgguNiYYk

class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        // 双指针，一个代表当前字符出现的第一个位置，一个表示修改后当前长度
        int left = 0, len = 0;
        for(int i = 0; i < n; i ++) {
            // 遇到临界点（最后一个位置，或者两字符分界处）
            if(i == n - 1 || chars[i] != chars[i + 1]) {
                chars[len ++] = chars[i];
                int nums = i - left + 1;
                if(nums > 1) {
                    // 把数字加到末尾
                    for(char num : to_string(nums)) {
                        chars[len ++] = num;
                    }
                }
                left = i + 1;
            }
        }
        return len;
    }
};

作者：heroding
链接：https://leetcode.cn/problems/string-compression/solution/cshuang-zhi-zhen-xiang-jie-by-heroding-tb7x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。