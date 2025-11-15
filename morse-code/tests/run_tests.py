# run_tests.py

import subprocess
import sys

TESTS = [
    "tests/test_tables.py",
    "tests/test_codec.py",
    "tests/test_detector.py",
]

print("Running Tests...\n")

all_passed = True

for test in TESTS:
    print(f"--- Running {test} ---")
    result = subprocess.run([sys.executable, "-m", test.replace(".py", "").replace("/", ".")])

    if result.returncode != 0:
        all_passed = False
        print(f"{test} FAILED\n")
    else:
        print(f"{test} passed\n")

if all_passed:
    print("ALL TESTS PASSED")
else:
    print("SOME TESTS FAILED")
