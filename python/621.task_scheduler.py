
"""
问题解析：
给定一个表示CPU需要做的任务的字符数组。它包含大写字母A到Z，其中不同的字母表示不同的任务。任务完成顺序不限。
每个任务可以在一个时间内完成，对于每个时间，CPU可以完成一个任务或空闲。
但是，在两个相同的任务之间有一个冷却时间间隔n，即两个相同任务之间至少必须有n个冷却时间间隔，
其中的间隔内CPU可以执行其他不同的任务或是处于空闲状态。
返回CPU完成所有给定任务所需的最小时间.
The figure in https://leetcode.com/articles/task-scheduler/
is clear to show the process

很详细的解释： http://www.cnblogs.com/grandyang/p/7098764.html
"""
def leastInterval(self, tasks, N):
    task_counts = collections.Counter(tasks).values()
    M = max(task_counts)
    Mct = task_counts.count(M)
    return max(len(tasks), (M - 1) * (N + 1) + Mct)