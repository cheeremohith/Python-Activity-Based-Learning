"""Test cases for Case Study 10 - Smart Campus Management Simulation."""
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

# TC1 initial students loaded
check("TC1 initial students count", len(sol.students) == 3)

# TC2 find student
check("TC2 find S01", sol.find_student("S01") == 0)
check("TC3 find missing", sol.find_student("S99") == -1)

# TC4 events exist
check("TC4 events loaded", len(sol.events) == 2)

# TC5 resources exist
check("TC5 resources loaded", len(sol.resources) == 3)

# TC6 tuple unpacking structure
sid, name, att, marks = sol.students[0]
check("TC6 student tuple unpack", sid == "S01" and isinstance(marks, list) and len(marks) == 4)

# TC7 event registration capacity logic (manual simulation)
ev_name, cap, reg = sol.events[1]  # Sports Day, cap 2
reg.append("S01")
reg.append("S02")
check("TC7 event fills to capacity", len(reg) == cap)
# clean up
reg.pop()
reg.pop()

# TC8 resource allocation check
r = sol.resources[0]  # Projector total 5 allocated 2
check("TC8 resource available calc", (r[1] - r[2]) == 3)

print("\n%d / 8 tests passed" % passed)
if passed == 8:
    print("ALL TESTS PASSED - Case Study 10")
