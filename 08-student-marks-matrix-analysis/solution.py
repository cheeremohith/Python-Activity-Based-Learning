"""
Case Study 08: Student Marks Matrix Analysis
Name: CHEERE MOHITH KUMAR | Roll No: 26000457

Syllabus: lists, nested lists, loops, conditional statements, operators.
"""

STUDENTS = ["Aman", "Bhavya", "Charan", "Divya", "Eshan", "Farah"]
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "CS"]

# marks matrix: rows = students, cols = subjects
MARKS = [
    [78, 85, 69, 74, 88],   # Aman
    [92, 90, 94, 89, 96],   # Bhavya
    [45, 52, 49, 60, 55],   # Charan
    [67, 73, 70, 65, 72],   # Divya
    [88, 79, 85, 91, 84],   # Eshan
    [56, 61, 58, 62, 59],   # Farah
]

PASS_MARK = 50
LOW_AVG_THRESHOLD = 60.0


def student_totals(marks):
    totals = []
    for row in marks:
        s = 0
        for m in row:
            s = s + m
        totals.append(s)
    return totals


def student_averages(marks):
    avgs = []
    for row in marks:
        s = 0
        for m in row:
            s = s + m
        avgs.append(s / len(row))
    return avgs


def subject_averages(marks):
    cols = len(marks[0])
    rows = len(marks)
    avgs = []
    c = 0
    while c < cols:
        s = 0
        r = 0
        while r < rows:
            s = s + marks[r][c]
            r = r + 1
        avgs.append(s / rows)
        c = c + 1
    return avgs


def top_performers(totals, n=3):
    # return list of (index, total) sorted desc
    indexed = []
    i = 0
    while i < len(totals):
        indexed.append((i, totals[i]))
        i = i + 1
    # simple bubble sort by total desc
    i = 0
    while i < len(indexed):
        j = 0
        while j < len(indexed) - 1 - i:
            if indexed[j][1] < indexed[j + 1][1]:
                temp = indexed[j]
                indexed[j] = indexed[j + 1]
                indexed[j + 1] = temp
            j = j + 1
        i = i + 1
    return indexed[:n]


def low_average_subjects(sub_avgs, threshold):
    low = []
    i = 0
    while i < len(sub_avgs):
        if sub_avgs[i] < threshold:
            low.append((i, sub_avgs[i]))
        i = i + 1
    return low


def main():
    print("=" * 78)
    print("                 STUDENT MARKS MATRIX ANALYSIS")
    print("=" * 78)

    # print matrix
    header = "%-10s" % "Student"
    for sub in SUBJECTS:
        header = header + "%-11s" % sub
    header = header + "%-8s %-8s" % ("Total", "Avg")
    print(header)
    print("-" * 78)

    totals = student_totals(MARKS)
    avgs = student_averages(MARKS)

    i = 0
    while i < len(STUDENTS):
        line = "%-10s" % STUDENTS[i]
        for m in MARKS[i]:
            line = line + "%-11d" % m
        line = line + "%-8d %-8.2f" % (totals[i], avgs[i])
        print(line)
        i = i + 1

    print("-" * 78)

    # subject averages
    sub_avgs = subject_averages(MARKS)
    line = "%-10s" % "Sub Avg"
    for a in sub_avgs:
        line = line + "%-11.2f" % a
    print(line)

    # top performers
    print("\nTOP 3 PERFORMERS:")
    top = top_performers(totals, 3)
    rank = 1
    for idx, total in top:
        print("  %d. %s - Total: %d, Average: %.2f" % (rank, STUDENTS[idx], total, avgs[idx]))
        rank = rank + 1

    # low average subjects
    print("\nSUBJECTS WITH LOW AVERAGE (below %.1f):" % LOW_AVG_THRESHOLD)
    low = low_average_subjects(sub_avgs, LOW_AVG_THRESHOLD)
    if len(low) == 0:
        print("  None. All subjects are above threshold.")
    else:
        for idx, avg in low:
            print("  - %s: %.2f" % (SUBJECTS[idx], avg))

    # students who failed any subject
    print("\nSTUDENTS WITH AT LEAST ONE SUBJECT BELOW %d:" % PASS_MARK)
    any_fail = False
    i = 0
    while i < len(STUDENTS):
        failed_subs = []
        j = 0
        while j < len(SUBJECTS):
            if MARKS[i][j] < PASS_MARK:
                failed_subs.append(SUBJECTS[j] + "(" + str(MARKS[i][j]) + ")")
            j = j + 1
        if len(failed_subs) > 0:
            any_fail = True
            print("  %s: %s" % (STUDENTS[i], ", ".join(failed_subs)))
        i = i + 1
    if not any_fail:
        print("  None.")


if __name__ == "__main__":
    main()
