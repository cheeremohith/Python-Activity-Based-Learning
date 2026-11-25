"""Test cases for Case Study 09 - Tuple-Based Course Registration Validation."""
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

valid_codes = sol.get_course_codes(sol.COURSE_CATALOG)

# TC1 valid registration
ok, issues = sol.validate_registration(sol.REGISTRATIONS[0], valid_codes)
check("TC1 Ravi valid", ok == True)

# TC2 duplicate detection
ok, issues = sol.validate_registration(sol.REGISTRATIONS[2], valid_codes)  # Mohan duplicate CS101
check("TC2 duplicate detected", ok == False and any("Duplicate" in i for i in issues))

# TC3 invalid combination
ok, issues = sol.validate_registration(sol.REGISTRATIONS[3], valid_codes)  # Neha CS101+CS201
check("TC3 invalid combo detected", ok == False and any("Invalid combination" in i for i in issues))

# TC4 unknown course
ok, issues = sol.validate_registration(sol.REGISTRATIONS[4], valid_codes)  # Arjun XX999
check("TC4 unknown course detected", ok == False and any("Unknown" in i for i in issues))

# TC5 another valid
ok, issues = sol.validate_registration(sol.REGISTRATIONS[1], valid_codes)
check("TC5 Sita valid", ok == True)

# TC6 find_duplicates helper
dups = sol.find_duplicates(("A","B","A","C","B"))
check("TC6 duplicates helper", "A" in dups and "B" in dups)

# TC7 catalog codes
check("TC7 catalog has 6 courses", len(valid_codes) == 6)

# TC8 overall counts
valid_count = 0
for r in sol.REGISTRATIONS:
    ok, _ = sol.validate_registration(r, valid_codes)
    if ok:
        valid_count += 1
check("TC8 3 valid out of 6", valid_count == 3)

print("\n%d / 8 tests passed" % passed)
if passed == 8:
    print("ALL TESTS PASSED - Case Study 09")
