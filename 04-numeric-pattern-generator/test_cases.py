"""Test cases for Case Study 04 - Advanced Numeric Pattern Generator."""
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

# TC1 valid odd size
lines, msg = sol.generate_hollow_diamond(5)
check("TC1 size 5 returns lines", lines is not None and msg == "OK")
check("TC2 size 5 has 5 rows", len(lines) == 5)

# TC2 even size rejected
lines, msg = sol.generate_hollow_diamond(4)
check("TC3 even size rejected", lines is None and "odd" in msg.lower())

# TC3 too small rejected
lines, msg = sol.generate_hollow_diamond(2)
check("TC4 size 2 rejected", lines is None)

# TC4 size 7
lines, msg = sol.generate_hollow_diamond(7)
check("TC5 size 7 has 7 rows", lines is not None and len(lines) == 7)

# TC5 middle row is widest
lines, msg = sol.generate_hollow_diamond(5)
mid = lines[2]  # 0-indexed middle
check("TC6 middle row has two edge digits", mid.strip()[0].isdigit() and mid.strip()[-1].isdigit())

# TC6 symmetry - top and bottom same
check("TC7 symmetric rows", lines[0] == lines[4] and lines[1] == lines[3])

# TC7 size 1 invalid
lines, msg = sol.generate_hollow_diamond(1)
check("TC8 size 1 rejected", lines is None)

print("\n%d / 8 tests passed" % passed)
if passed == 8:
    print("ALL TESTS PASSED - Case Study 04")
