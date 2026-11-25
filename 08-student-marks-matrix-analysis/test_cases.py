"""Test cases for Case Study 08 - Student Marks Matrix Analysis."""
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

totals = sol.student_totals(sol.MARKS)
avgs = sol.student_averages(sol.MARKS)
sub_avgs = sol.subject_averages(sol.MARKS)

# TC1 totals
check("TC1 Bhavya total 461", totals[1] == 461)

# TC2 average
check("TC2 Bhavya avg 92.2", abs(avgs[1] - 92.2) < 0.01)

# TC3 subject averages length
check("TC3 5 subject averages", len(sub_avgs) == 5)

# TC4 top performer
top = sol.top_performers(totals, 1)
check("TC4 top performer is Bhavya", top[0][0] == 1)

# TC5 low avg subjects (Chemistry is 70.83, all above 60?) compute
# Chemistry avg = (69+94+49+70+85+58)/6 = 70.833
low = sol.low_average_subjects(sub_avgs, 60.0)
check("TC5 no subject below 60 avg", len(low) == 0)

# TC6 student fail detection - Charan has 45 in Maths, 49 in Chem
charan_row = sol.MARKS[2]
has_fail = any(m < 50 for m in charan_row)
check("TC6 Charan has failing marks", has_fail == True)

# TC7 matrix shape
check("TC7 6 students", len(sol.MARKS) == 6)
check("TC8 5 subjects per student", all(len(r) == 5 for r in sol.MARKS))

print("\n%d / 8 tests passed" % passed)
if passed == 8:
    print("ALL TESTS PASSED - Case Study 08")
