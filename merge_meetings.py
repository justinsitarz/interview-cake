meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

def merge_meetings(meetings):
	merged_meetings = []
	for m in meetings:
		if not merged_meetings:
			merged_meetings.append(m)
		for mm in merged_meetings:
			if (m > mm[0] and m < mm[1]):
				mm[1] = m[1]
	print(merged_meetings)


merge_meetings(meetings)