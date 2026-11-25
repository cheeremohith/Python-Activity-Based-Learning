"""
Case Study 09: Tuple-Based Course Registration Validation
Name: CHEERE MOHITH KUMAR | Roll No: 26000457

Syllabus: tuples, tuple operations, tuple unpacking, lists, loops, conditionals, strings.
"""

# Course catalog: (course_code, course_name, credits)
COURSE_CATALOG = [
    ("CS101", "Programming Basics", 4),
    ("CS102", "Data Structures", 4),
    ("MA101", "Calculus", 3),
    ("PH101", "Physics", 3),
    ("EN101", "English", 2),
    ("CS201", "Algorithms", 4),
]

# Invalid combinations (cannot be taken together in same semester)
INVALID_COMBINATIONS = [
    ("CS101", "CS201"),  # CS201 needs CS102, but also treat as invalid combo here per rules
]

# Registration records: (student_id, student_name, registered_courses_tuple)
REGISTRATIONS = [
    ("26001", "Ravi",    ("CS101", "MA101", "PH101")),
    ("26002", "Sita",    ("CS101", "CS102", "EN101")),
    ("26003", "Mohan",   ("CS101", "MA101", "CS101")),   # duplicate
    ("26004", "Neha",    ("CS101", "CS201", "MA101")),   # invalid combo
    ("26005", "Arjun",   ("CS102", "MA101", "XX999")),   # unknown course
    ("26006", "Kiran",   ("EN101", "PH101")),
]


def get_course_codes(catalog):
    codes = []
    for c in catalog:
        code, name, credits = c
        codes.append(code)
    return codes


def find_duplicates(courses):
    seen = []
    dups = []
    for c in courses:
        if c in seen:
            if c not in dups:
                dups.append(c)
        else:
            seen.append(c)
    return dups


def find_invalid_combos(courses):
    bad = []
    for combo in INVALID_COMBINATIONS:
        a, b = combo
        if a in courses and b in courses:
            bad.append(combo)
    return bad


def find_unknown_courses(courses, valid_codes):
    unknown = []
    for c in courses:
        if c not in valid_codes:
            unknown.append(c)
    return unknown


def validate_registration(record, valid_codes):
    student_id, name, courses = record
    issues = []

    dups = find_duplicates(courses)
    if len(dups) > 0:
        issues.append("Duplicate registrations: " + ", ".join(dups))

    bad_combos = find_invalid_combos(courses)
    for a, b in bad_combos:
        issues.append("Invalid combination: %s and %s cannot be taken together" % (a, b))

    unknown = find_unknown_courses(courses, valid_codes)
    if len(unknown) > 0:
        issues.append("Unknown course code(s): " + ", ".join(unknown))

    is_valid = (len(issues) == 0)
    return is_valid, issues


def main():
    valid_codes = get_course_codes(COURSE_CATALOG)

    print("=" * 74)
    print("        TUPLE-BASED COURSE REGISTRATION VALIDATION")
    print("=" * 74)

    print("Course Catalog:")
    for c in COURSE_CATALOG:
        code, name, credits = c
        print("  %s - %s (%d credits)" % (code, name, credits))

    print("\nInvalid combinations:")
    for a, b in INVALID_COMBINATIONS:
        print("  - %s + %s" % (a, b))

    print("\n" + "-" * 74)
    print("VALIDATION RESULTS:")
    print("-" * 74)

    valid_count = 0
    invalid_count = 0

    for rec in REGISTRATIONS:
        sid, name, courses = rec
        ok, issues = validate_registration(rec, valid_codes)
        status = "VALID" if ok else "INVALID"
        print("\nStudent: %s (%s)" % (name, sid))
        print("  Courses :", ", ".join(courses))
        print("  Status  :", status)
        if ok:
            valid_count = valid_count + 1
        else:
            invalid_count = invalid_count + 1
            for issue in issues:
                print("  - " + issue)

    print("\n" + "=" * 74)
    print("SUMMARY: Total=%d, Valid=%d, Invalid=%d" %
          (len(REGISTRATIONS), valid_count, invalid_count))


if __name__ == "__main__":
    main()
