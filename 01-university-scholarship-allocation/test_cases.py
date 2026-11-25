"""Test cases for Case Study 01 - University Scholarship Allocation."""
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

# TC1 - fully eligible student
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[0])  # S101 Ananya
check("TC1 S101 eligible", ok == True)
check("TC1 S101 aggregate near 80.8", abs(agg - 80.8) < 0.01)

# TC2 - aggregate below minimum
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[1])  # S102
check("TC2 S102 rejected for low aggregate", ok == False and any("Aggregate" in r for r in reasons))

# TC3 - subject-wise failure
check("TC3 S102 has Physics below minimum", any("Physics" in r for r in reasons))

# TC4 - income above limit
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[2])  # S103
check("TC4 S103 rejected for income", ok == False and any("income" in r.lower() for r in reasons))

# TC5 - attendance below minimum
ok, agg, reasons = sol.check_applicant(sol.APPLICANTS[5])  # S106
check("TC5 S106 rejected for attendance", ok == False and any("Attendance" in r for r in reasons))

# TC6 - ranking: top student should be S105
eligible = []
for a in sol.APPLICANTS:
    ok, agg, rs = sol.check_applicant(a)
    if ok:
        roll, name, marks, att, inc = a
        eligible.append((roll, name, round(agg, 2), att, inc))
eligible.sort(key=sol.sort_key)
check("TC6 S105 ranked first", eligible[0][0] == "S105")

# TC7 - tie resolved by attendance (S108 vs S104 both 61.4)
pos108 = -1
pos104 = -1
for i, rec in enumerate(eligible):
    if rec[0] == "S108":
        pos108 = i
    if rec[0] == "S104":
        pos104 = i
check("TC7 tie broken by attendance (S108 before S104)", pos108 != -1 and pos104 != -1 and pos108 < pos104 and eligible[pos108][2] == eligible[pos104][2])

# TC8 - counts
total_ok = 0
for a in sol.APPLICANTS:
    ok, agg, rs = sol.check_applicant(a)
    if ok:
        total_ok += 1
check("TC8 4 eligible and 4 rejected", total_ok == 4 and len(sol.APPLICANTS) - total_ok == 4)

print("\n%d / 9 tests passed" % passed)
if passed == 9:
    print("ALL TESTS PASSED - Case Study 01")
