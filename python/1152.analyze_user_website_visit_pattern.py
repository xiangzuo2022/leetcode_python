

# Abu Shoeb 2020-07-16
# Runtime: 52 ms, faster than 82.74% of Python3 online submissions for Analyze User Website Visit Pattern.
# Memory Usage: 14.6 MB, less than 24.50% of Python3 online submissions for Analyze User Website Visit Pattern.
		
import itertools as it
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
		# step1 - sorting and keeping the result as lists
		timestamp, username, website = (list(t) for t in zip(*sorted(zip(timestamp, username, website))))

        # step2 - form a dictionary; users as key and website list as value
		user_and_web = {}
        for i in range(len(username)):
            if username[i] in user_and_web:
                user_and_web[username[i]].append(website[i])
            else:
                user_and_web[username[i]] = [website[i]]
		
		# step3 - form another dictionary where 3-sequence of websites as key and their counts as value
        sequence = {}
        for key in user_and_web:
            if len(user_and_web[key]) >= 3:
                temp = set(it.combinations(user_and_web[key], r=3))
                for t in temp:
                    if t in sequence:
                        sequence[t] += 1
                    else:
                        sequence[t] = 1
		
		# step4 - sort the sequence dictionary and return only the first element
        return sorted(sequence, key=lambda k: (-sequence[k], k))[0]
  
"""
my own code
"""    
import itertools as it
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        timestamp, username, website = (list(t) for t in zip(*sorted(zip(timestamp, username, website))))
        maps = {}
        n = len(username)
        for i in range(n):
            if username[i] in maps:
                maps[username[i]].append(website[i])
            else:
                maps[username[i]] = [website[i]]
        sequence = {}
        for key in maps:
            if len(maps[key]) >= 3:
                temp = set(it.combinations(maps[key], r=3))
                for t in temp:
                    if t in sequence:
                        sequence[t] += 1
                    else:
                        sequence[t] = 1
        
        return sorted(sequence, key=lambda k:(-sequence[k], k))[0]