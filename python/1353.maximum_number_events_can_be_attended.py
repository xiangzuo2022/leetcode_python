"""
"""
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(key = lambda e: e[0])
        pq = [] # store end time of open events
        count = 0
        i, n = 0, len(events)
        currDay = 1  # current day
        
        while i < n or pq:  
            #将所有开始时间等于 currDay 的会议的结束时间放到小顶堆         
            while i < n and currDay == events[i][0]: # push all events we can possibly attend
                heappush(pq, events[i][1])
                i += 1
            # 将已经结束的会议弹出堆中，即堆顶的结束时间小于 currDay 的
            while pq and pq[0] < currDay: # remove all impossible-to-attend events
                heappop(pq)
            # 贪心的选择结束时间最小的会议参加
            if pq:
                # 参加的会议，就从堆中删除
                heappop(pq)
                count += 1
           # 当前的天往前走一天，开始看下下一天能不能参加会议
            currDay += 1
           
        return count