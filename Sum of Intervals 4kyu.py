def sum_of_intervals(intervals):
    total = 0
    registeredRanges = []
    for interval in intervals:
        overlappingLow, overlappingHigh = {'bool': False, 'position': 0}, {'bool': False, 'position': 0}
        for i, range in enumerate(registeredRanges):
            if range[0] < interval[0] < range[1]:
                overlappingLow['bool'] = True
                overlappingLow['position'] = i
            if range[0] < interval[1] < range[1]:
                overlappingHigh['bool'] = True
                overlappingHigh['position'] = i

        if overlappingLow['bool'] or overlappingHigh['bool']:
            if overlappingHigh['bool']:
                registeredRanges[overlappingHigh['position']][0] = interval[0]
            elif overlappingLow['bool']:
                registeredRanges[overlappingLow['position']][1] = interval[1]
        else:
            if list(interval) not in registeredRanges:
                registeredRanges.append(list(interval))

    for interval in registeredRanges:
        total += abs(interval[1] - interval[0])

    print(registeredRanges)
    return total


print(sum_of_intervals([(-4, 4), (7, 10), (3, 5)]))
