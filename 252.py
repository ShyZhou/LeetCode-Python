# Meeting Rooms

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

class Solution(object):
    def canAttendMeeting(self, meeting_times):
        meeting_times.sort(key=lambda x: x[0])
        for i in range(1, len(meeting_times)):
            if meeting_times[i][0] < meeting_times[i - 1][1]:
                return False
        return True

# II

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

class Solution(object):
    def minRooms(self, meeting_times):
        start = [time[0] for time in meeting_times]
        end = [time[1] for time in meeting_times]

        start.sort()
        end.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                cnt_rooms += 1 # Acquire a room
                min_rooms = min(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1 # Release a room
                e += 1
        return min_rooms

sol = Solution()
print(sol.canAttendMeeting(meeting_times=[[0, 30],[15, 20],[5, 10]]))

