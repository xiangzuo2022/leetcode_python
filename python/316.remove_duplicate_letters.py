class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 统计每个字符出现的次数
        # 每个字符是否使用，由于只保留一个，所以这地方最多需要26个。
        vis, cnt = [False] * 26, [0] * 26
        ans = []
        for c in s:
            cnt[ord(c) - 97] += 1  # ord(a) =97
        for c in s:
            index = ord(c) - 97
            cnt[index] -= 1
            # 结果集里已经有了，不需要再放进来了。
            if vis[index]: 
                continue
            #优化步骤
            while ans and ans[-1] > c and cnt[ord(ans[-1]) - 97]:
                #  后面有更好的，则删除，设置为没有用过。
                vis[ord(ans.pop()) - 97] = False
            # 更新状态
            ans.append(c)
            vis[index] = True
 
        return ''.join(ans)