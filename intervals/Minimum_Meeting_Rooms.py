class MeetingRooms:
    def minMeetingRooms(self, intervals):
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s<len(intervals):
            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e += 1
                count-=1
            res = max(res, count)
        return res

if __name__ == "__main__":
    meetings = MeetingRooms()
    intervals = [(0,30),(5,10),(15,20)] 
    rooms_needed = meetings.minMeetingRooms(intervals)
    print(rooms_needed)
