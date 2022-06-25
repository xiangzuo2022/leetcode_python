"""
The idea is: for every character, we can keep it or abbreviate it. To keep it, 
we add it to the current solution and carry on backtracking. To abbreviate it, 
we omit it in the current solution, but increment the count, which indicates how many 
characters have we abbreviated. When we reach the end or need to put a character in 
the current solution, and count is bigger than zero, we add the number into the solution.
"""
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, result)
                # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result

"""
concise code    
"""
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(depth, value, count):
            if len(word) == depth:
                # Once we reach the end, append current to the result
                result.append(value + str(count) if count > 0 else value)
            else:
                # Skip current position, and increment count
                helper(depth + 1, value, count + 1)
                # Include current position, and zero-out count
                helper(depth + 1, value + (str(count) if count > 0 else '') + word[depth], 0)

        result = []
        helper(0, '', 0)
        return result