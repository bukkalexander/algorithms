N = 0


def interval_scheduling(intervals):
    # Select as many non-overlapping (disjoint) intervals as possible
    disjoint_intervals = set()
    return check_interval(intervals, disjoint_intervals)


def check_interval(intervals, disjoint_intervals):
    global N
    N = N + 1
    max_candidate_solution = 0
    for interval in intervals:
        if not is_overlapping_any_interval(interval, disjoint_intervals):
            candidate_solution = check_interval(
                intervals.difference({interval}),
                disjoint_intervals.union({interval})
            ).union({interval})
            if len(candidate_solution) > max_candidate_solution:
                disjoint_intervals = candidate_solution
                max_candidate_solution = len(candidate_solution)
    return disjoint_intervals


def is_overlapping_any_interval(interval, interval_set):
    for i in interval_set:
        if interval[0] < i[1] and interval[1] > i[0]:
            # interval is overlapping
            return True
    return False


def main():
    intervals = {
        (0, 2),
        (1, 4),
        (2, 4),
        (4, 5),
        (3, 5),
        (3, 6),
        (4, 7),
        (5, 7),
        (7, 8),
        (8, 9),
        (9, 10),
    }
    print("Intervals:")
    print(intervals)
    disjoint_intervals = interval_scheduling(intervals)
    n_disjoint_intervals = len(disjoint_intervals)
    print("\nMax number of disjoint intervals: " + str(n_disjoint_intervals))
    print("Disjoint intervals:")
    print(disjoint_intervals)
    print(str(N))

if __name__ == "__main__":
    main()
