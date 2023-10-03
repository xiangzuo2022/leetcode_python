"""
本题的题意开始没理解好，其实就是给出按照字典序排序好的一堆单词，让你根据这堆单词，找出此语言中已知字母的顺序。
所以我们可以得到思路：将词典中字符串的字符两两对比，只有第一个不同的字符才是正确的排序，如ert和wrf，只能推断
出e的优先级高于w（e   − >   w e\ ->\ we −> w），剩余字符的优先级不能推断。
(拓扑排序) O(n)
建图：遍历所有单词将第一个不同字母设为边。
“wfc”, “wfa” 可得边 ‘c’ 到 ‘a’。由于使用了矩阵过滤掉重边。
注意如果有非法顺序例如 “abc”, “ab” 则直接返回无解。
所有其他出现但无顺序信息的字母标记为已出现（v)，入度不更新。

建图完成后直接根据入度拓扑排序。
"""
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
    

# https://www.youtube.com/watch?v=6kTZYvNNyps
# topological sort DAG
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # False=visited, True=current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)