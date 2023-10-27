def merge(intervals):
    intervals.sort()
    output = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start,end])
    return output

if __name__ == "__main__":
	intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
	print(merge(intervals))
