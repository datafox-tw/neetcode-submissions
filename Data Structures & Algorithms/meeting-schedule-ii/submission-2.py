"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        days = 0
        items = [] #存已經被用過的intervals
        while len(intervals)>0:
            days += 1
            today_agenda = [intervals[0]]
            for i in range(1, len(intervals)):
                if today_agenda[-1].end <= intervals[i].start:
                    today_agenda.append(intervals[i])
            print(today_agenda)
            for i in today_agenda:
                intervals.remove(i)
        return days



        # while count < len(intervals)
        #     today_agenda = []
        #     for i in range(1, len(intervals)):
        #         if len(today_agenda) == 0:
        #             today_agenda.append
        #         i1 = intervals[i - 1]
        #         i2 = intervals[i]
        #         if i1.end <= i2.start:
        #             today_agenda.append()
        # return True

        # res = 0
        # prevEnd = intervals[0][1]
        # print(intervals)
        # for start, end in intervals[1:]:
        #     if start >= prevEnd:
        #         prevEnd = end
        #     else:
        #         res += 1
        #         prevEnd = min(end, prevEnd)
        # return res
