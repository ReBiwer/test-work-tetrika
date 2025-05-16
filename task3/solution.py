def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals)
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged

def intersect_intervals(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])
        if start < end:
            result.append([start, end])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return result

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    lesson_interval = [[lesson[0], lesson[1]]]
    pupil_intervals = [[pupil[i], pupil[i+1]] for i in range(0, len(pupil), 2)]
    tutor_intervals = [[tutor[i], tutor[i+1]] for i in range(0, len(tutor), 2)]
    pupil_merged = merge_intervals(pupil_intervals)
    tutor_merged = merge_intervals(tutor_intervals)
    both = intersect_intervals(pupil_merged, tutor_merged)
    both_in_lesson = intersect_intervals(both, lesson_interval)
    return sum(end - start for start, end in both_in_lesson) 