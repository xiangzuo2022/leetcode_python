"""
First split input string by "\n" into a list containing directory and file names. Loop through the list. Everytime a file (contianing ".") is encountered, the length of the file path is noted. The maximum length is returned.

The key is to keep track of all parent directories of every file. We can do so with a stack. The depth (count "\t") can only increase 1 at a time. If the depth of an item decreases, we pop the stack until what remains on top of stack is an immediate parent directory of the item.
"""

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen


"""
readable code
"""
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        ans = lengthSum = 0
        stack = [(-1, 0)]
        for p in input.split('\n'):
            depth = p.count('\t')
            name = p.replace('\t', '')
            topDepth, topLength = stack[-1]
            while depth <= topDepth:
                stack.pop()
                lengthSum -= topLength
                topDepth, topLength = stack[-1]
            length = len(name) + (depth > 0)
            lengthSum += length
            stack.append((depth, length))
            if name.count('.'):
                ans = max(ans, lengthSum)
        return ans