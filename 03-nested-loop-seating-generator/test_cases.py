"""Test cases for Case Study 03 - Nested Loop Examination Seating Generator."""
import importlib.util, os
spec = importlib.util.spec_from_file_location("sol", os.path.join(os.path.dirname(__file__), "solution.py"))
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)

passed = 0
def check(name, cond):
    global passed
    if cond:
        passed += 1
        print("PASS:", name)
    else:
        print("FAIL:", name)

seating, stats = sol.generate_seating(sol.ROWS, sol.COLS, sol.ROLL_NUMBERS)

# TC1 dimensions
check("TC1 correct number of rows", len(seating) == sol.ROWS)
check("TC2 correct number of cols", len(seating[0]) == sol.COLS)

# TC2 reserved positions
check("TC3 reserved (1,2)", seating[0][1] == "RESV")
check("TC4 reserved (2,4)", seating[1][3] == "RESV")
check("TC5 reserved (4,1)", seating[3][0] == "RESV")

# TC3 stats consistency
check("TC6 total seats", stats["total"] == 30)
check("TC7 filled count matches placed rolls", stats["filled"] <= len(sol.ROLL_NUMBERS))

# TC4 no roll number in reserved/blocked
ok = True
for r in range(sol.ROWS):
    for c in range(sol.COLS):
        if sol.is_reserved(r+1, c+1):
            if seating[r][c] != "RESV":
                ok = False
check("TC8 reserved cells not overwritten", ok)

print("\n%d / 8 tests passed" % passed)
if passed == 8:
    print("ALL TESTS PASSED - Case Study 03")
