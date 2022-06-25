"""
数组delete不能做到O(1),所以用dic
思路：用hash记录下标， 删除只需要和末尾元素调换即可
"""
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.ind = [], {}
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ind: 
            self.nums += val, 
            self.ind[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ind:
            ind, last = self.ind[val], self.nums[-1]
            self.nums[ind], self.ind[last] = last, ind #把要delete的element放到array的最后一个位置 
            self.nums.pop() # O(1)
            self.ind.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)
      
"""
Why hashmap is not a good choice: the problem is in getRandom where we need a group of index while hashmap does not have
any indexes. Converting has keys to indexes needs linear time while our purpose is constatnt time.
leetcode solution explonation is good 
"""
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = []
        self.dic = {}        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.num.append(val)
        self.dic[val] = len(self.num) - 1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        index, last_element = self.dic[val], self.num[-1]
        self.num[index], self.dic[last_element] = last_element, index # 其实并没有实现真正的交换，只是把最后一个元素的值放了过来， 在一段时间里最后一个值出现2次
        self.num.pop()
        self.dic.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return choice(self.num)
        
