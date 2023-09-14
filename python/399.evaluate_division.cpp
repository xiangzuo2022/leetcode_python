class Solution {
public:
    unordered_map<string, vector<pair<string, double>>> graph;
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        
        int n = equations.size();
        for (int i = 0; i < n; i++) {
            string a = equations[i][0];
            string b = equations[i][1];
            double val = values[i];
            
            graph[a].push_back({b, val});
            graph[b].push_back({a, (double)1/val});
        }
        
        vector<double> result;
        for (auto query : queries) {
            unordered_set<string> visited;
            result.push_back(dfs(query[0], query[1], visited));
        }
        return result;
    }
    
    double dfs(string src, string dst, unordered_set<string> &visited) {
        if (graph.find(src) == graph.end()) return -1;
        if (src == dst) return 1;
        
        for (auto node : graph[src]) {
            if (visited.count(node.first)) continue;
            visited.insert(node.first);
            double res = dfs(node.first, dst, visited);
            if (res != -1) return res * node.second;
        }
        return -1;
    }
};

https://www.youtube.com/watch?v=hDUj0W5Rtxs&list=PLwdV8xC1EWHrtgsYCcDTXIMVaHSlsnLzL&index=974

# https://www.youtube.com/watch?v=Uei1fwDoyKk
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q = deque()
            visit = set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1
        return [bfs(q[0], q[1]) for q in queries]