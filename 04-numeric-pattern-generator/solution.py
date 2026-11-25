"""
Case Study 04: Advanced Numeric Pattern Generator
Name: CHEERE MOHITH KUMAR | Roll No: 26000457

Syllabus: loops, nested loops, conditional statements, operators, strings.
"""

def generate_hollow_diamond(n):
    """Generate a hollow diamond pattern of size n (n must be odd and >= 3)."""
    if n < 3:
        return None, "Error: size must be at least 3."
    if n % 2 == 0:
        return None, "Error: size must be an odd number for a symmetric diamond."

    mid = n // 2
    lines = []

    # top half including middle
    for i in range(mid + 1):
        row = ""
        for j in range(n):
            # distance from center
            if j == mid - i or j == mid + i:
                # use number based on row position
                val = (i % 9) + 1
                row = row + str(val)
            else:
                row = row + " "
        lines.append(row.rstrip())

    # bottom half
    for i in range(mid - 1, -1, -1):
        row = ""
        for j in range(n):
            if j == mid - i or j == mid + i:
                val = (i % 9) + 1
                row = row + str(val)
            else:
                row = row + " "
        lines.append(row.rstrip())

    return lines, "OK"


def print_pattern(lines):
    for line in lines:
        print(line)


def main():
    print("=" * 55)
    print("       ADVANCED NUMERIC PATTERN GENERATOR")
    print("=" * 55)

    test_sizes = [5, 7, 4, 2]

    for n in test_sizes:
        print("\nRequested size: %d" % n)
        print("-" * 30)
        lines, msg = generate_hollow_diamond(n)
        if lines is None:
            print(msg)
        else:
            print("Hollow Diamond (size %d):" % n)
            print_pattern(lines)
            print("Rows generated: %d" % len(lines))

    # also show a default pattern
    print("\n" + "=" * 55)
    print("Default pattern (size 9):")
    print("-" * 30)
    lines, msg = generate_hollow_diamond(9)
    if lines is not None:
        print_pattern(lines)


if __name__ == "__main__":
    main()
