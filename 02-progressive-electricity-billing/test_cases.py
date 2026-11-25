"""Test cases for Case Study 02 - Progressive Electricity Billing."""
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

# TC1: 95 units - slab1 only with rebate
energy, fixed, sur, reb, total = sol.calculate_bill(95)
check("TC1 95 units energy 142.5", abs(energy - 142.5) < 0.01)
check("TC1 95 units rebate applied", reb > 0 and sur == 0)
check("TC1 95 units total", abs(total - 185.38) < 0.05)

# TC2: 120 units - crosses slab 1
energy, fixed, sur, reb, total = sol.calculate_bill(120)
check("TC2 120 units energy 200.0", abs(energy - 200.0) < 0.01)
check("TC2 120 units no rebate no surcharge", reb == 0 and sur == 0)

# TC3: 530 units - surcharge applies
energy, fixed, sur, reb, total = sol.calculate_bill(530)
check("TC3 530 units surcharge applied", sur > 0)
check("TC3 530 units energy 1980.0", abs(energy - 1980.0) < 0.01)

# TC4: 680 units - high surcharge
energy, fixed, sur, reb, total = sol.calculate_bill(680)
check("TC4 680 units energy 2880.0", abs(energy - 2880.0) < 0.01)

# TC5: fixed charge always added
_, fixed, _, _, total = sol.calculate_bill(0)
check("TC5 zero units gives fixed charge only", abs(total - 50.0) < 0.01)

print("\n%d / 9 tests passed" % passed)
if passed == 9:
    print("ALL TESTS PASSED - Case Study 02")
