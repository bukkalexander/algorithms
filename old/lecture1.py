def naive_interval_scheduling(intervals):
    # Select as many non-overlapping (disjoint) intervals as possible
    disjoint_intervals = set()
    return check_interval(intervals, disjoint_intervals)


def check_interval(intervals, disjoint_intervals):
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


def eef_interval_scheduling(interval_list):
    disjoint_interval_list = list()
    interval_list.sort(key=lambda x: x[1])

    f = 0  # interval end
    for interval in interval_list:
        if interval[0] < f:
            continue
        else:
            disjoint_interval_list.append(interval)
            f = interval[1]

    return disjoint_interval_list


def main():
    # ==================================================================================================================
    # Interval scheduling instance
    # ==================================================================================================================
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

    # ==================================================================================================================
    # Naive interval scheduling
    # ==================================================================================================================
    print()
    print("=" * 80)
    print("Naive interval scheduling")
    print("=" * 80)
    disjoint_intervals = naive_interval_scheduling(intervals)
    n_disjoint_intervals = len(disjoint_intervals)
    print("\nMax number of disjoint intervals: " + str(n_disjoint_intervals))
    print("Disjoint intervals:")
    disjoint_intervals = list(disjoint_intervals)
    disjoint_intervals.sort(key=lambda x: x[1])
    print(disjoint_intervals)

    # ==================================================================================================================
    # EEF (earliest end first) interval scheduling
    # ==================================================================================================================
    print()
    print("="*80)
    print("EEF (earliest end first) interval scheduling")
    print("=" * 80)
    disjoint_intervals = eef_interval_scheduling(list(intervals))
    n_disjoint_intervals = len(disjoint_intervals)
    print("\nMax number of disjoint intervals: " + str(n_disjoint_intervals))
    print("Disjoint intervals:")
    print(disjoint_intervals)


if __name__ == "__main__":
    main()
