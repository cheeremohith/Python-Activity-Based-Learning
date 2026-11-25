"""Test cases for Case Study 06 - RLE Compression."""
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

# TC1 basic encoding
check("TC1 basic encode", sol.rle_encode("AAABBBCCDAA") == "A3B3C2D1A2")

# TC2 decode back
enc = sol.rle_encode("AAABBBCCDAA")
check("TC2 decode matches", sol.rle_decode(enc) == "AAABBBCCDAA")

# TC3 no-benefit case
enc2 = sol.rle_encode("ABCD")
_, _, _, beneficial = sol.compression_info("ABCD", enc2)
check("TC3 ABCD not beneficial", beneficial == False)

# TC4 beneficial case
enc3 = sol.rle_encode("AAAAAA")
_, _, _, beneficial = sol.compression_info("AAAAAA", enc3)
check("TC4 AAAAAA beneficial", beneficial == True)

# TC5 empty string
check("TC5 empty encode", sol.rle_encode("") == "")

# TC6 single char
check("TC6 single char", sol.rle_encode("Z") == "Z1")

# TC7 round trip
s = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
check("TC7 round trip long", sol.rle_decode(sol.rle_encode(s)) == s)

# TC8 compression info lengths
o, e, sav, ben = sol.compression_info("AABBAABB", sol.rle_encode("AABBAABB"))
check("TC8 lengths correct", o == 8 and e == 8)

print("\n%d / 8 tests passed" % passed)
if passed == 8:
    print("ALL TESTS PASSED - Case Study 06")
