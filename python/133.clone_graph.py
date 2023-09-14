# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
    	def dfs(self, input, map):
    		if input in map:
    			return map[input]
    		output = UndirectedGraphNode(input.label)
    		map[input] = output
    		for neighbor in input.neighbors:
    			output.neighbors.append(dfs(neighbor,map))
    		return output
    	if not node:
    		return None
    	return self.dfs(node,{})



#  ********** The Second Time ***********
"""
# 解题思路：由于遍历一个图有两种方式：bfs和dfs。所以深拷贝一个图也可以采用这两种方法。不管使用dfs还是bfs
# 都需要一个哈希表map来存储原图中的节点和新图中的节点的一一映射。map的作用在于替代bfs和dfs中的visit数组，
# 一旦map中出现了映射关系，就说明已经复制完成，也就是已经访问过了。
# 输入和输出都是一个node， 通过node可以找到图中所有的点和它们的neighbors
"""


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
"""
# 解法-： dfs
输入输出都是node
"""
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node): # 输入和输出都是一个node
        def dfs(input,map):
            if input in map:
                return map[input]
            output = UndirectedGraphNode(input.label)
            map[input] = output
            for neighbor in input.neighbors:
                output.neighbors.append(dfs(neighbor,map))            
            return output

        if node == None: return None
        return dfs(node,{})

"""
# 解法二：bfs
"""
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @BFS
    def cloneGraph(self, node):
        if node == None: return None
        queue = []; map = {}
        newhead = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = newhead
        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    copy = UndirectedGraphNode(neighbor.label)
                    map[curr].neighbors.append(copy)
                    map[neighbor] = copy
                    queue.append(neighbor)
                else:
                    # turn directed graph to undirected graph
                    map[curr].neighbors.append(map[neighbor])
        return newhead


"""
python3 version: BFS
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = []
        map = {} # store both nodes and edges
        newhead = Node(node.val, [])
        queue.append(node)
        map[node] = newhead
        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    copy = Node(neighbor.val,[])
                    map[curr].neighbors.append(copy)
                    map[neighbor] = copy
                    queue.append(neighbor)
                else:
                    map[curr].neighbors.append(map[neighbor])
        return newhead






class Solution {
    unordered_map<Node*, Node*>Map;
public:
    Node* cloneGraph(Node* node) 
    {   
        if(node == NULL)return node;
        if (Map.find(node)!=Map.end())
            return Map[node];
            
        Node* newNode = new Node(node->val);
        Map[node] = newNode;
        
        for (int i=0; i<node->neighbors.size(); i++)
        {
            newNode->neighbors.push_back(cloneGraph(node->neighbors[i]));
        }
        
        return newNode;
    }

};
https://www.youtube.com/watch?v=yE4qcjabHqY&t=450s


# https://www.youtube.com/watch?v=mQeF6bN8hMk
# DFS + Hashmap
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {}
        
        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None












