"""Test cases for Case Study 05 - Password Policy Validation Engine."""
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

# TC1 valid password
ok, fails = sol.validate_password("Hello@123")
check("TC1 valid password accepted", ok == True and len(fails) == 0)

# TC2 missing uppercase/special
ok, fails = sol.validate_password("hello123")
check("TC2 missing upper/special detected", ok == False)

# TC3 too short
ok, fails = sol.validate_password("Abc@1")
check("TC3 short password rejected", ok == False and any("Length" in f or "minimum" in f for f in fails))

# TC4 prohibited substring
ok, fails = sol.validate_password("MyAdmin@2024")
check("TC4 prohibited substring detected", ok == False and any("prohibited" in f.lower() for f in fails))

# TC5 repeated chars
ok, fails = sol.validate_password("AAAbbb@123")
check("TC5 repeated chars detected", ok == False and any("repeat" in f.lower() or "same character" in f.lower() or "row" in f.lower() for f in fails))

# TC6 missing digit
ok, fails = sol.validate_password("NoDigit@Here")
check("TC6 missing digit detected", ok == False and any("digit" in f.lower() for f in fails))

# TC7 another valid
ok, fails = sol.validate_password("Strong$Pass7")
check("TC7 strong password accepted", ok == True)

# TC8 prohibited 'password'
ok, fails = sol.validate_password("PASSWORD@1")
check("TC8 contains 'password' rejected", ok == False)

print("\n%d / 8 tests passed" % passed)
if passed == 8:
    print("ALL TESTS PASSED - Case Study 05")
