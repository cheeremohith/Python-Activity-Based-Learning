"""Test cases for Case Study 07 - ATM Banking Simulation."""
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

# TC1 deposit works
bal = 5000.0
log = []
bal, ok, msg = sol.deposit(bal, log, 2000)
check("TC1 deposit accepted", ok == True and bal == 7000.0)

# TC2 withdraw works
bal, ok, msg = sol.withdraw(bal, log, 1000)
check("TC2 withdraw accepted", ok == True and bal == 6000.0)

# TC3 withdraw not multiple of 100
bal2, ok, msg = sol.withdraw(bal, log, 1050)
check("TC3 non-multiple rejected", ok == False)

# TC4 withdraw over limit
bal2, ok, msg = sol.withdraw(bal, log, 12000)
check("TC4 over limit rejected", ok == False)

# TC5 min balance violation
bal2, ok, msg = sol.withdraw(bal, log, 5500)  # would leave 500
check("TC5 min balance protected", ok == False)

# TC6 negative deposit
bal2, ok, msg = sol.deposit(bal, log, -500)
check("TC6 negative deposit rejected", ok == False)

# TC7 large deposit rejected
bal2, ok, msg = sol.deposit(bal, log, 200000)
check("TC7 over deposit limit rejected", ok == False)

# TC8 log records
check("TC8 log has 2 transactions", len(log) == 2)

print("\n%d / 8 tests passed" % passed)
if passed == 8:
    print("ALL TESTS PASSED - Case Study 07")
