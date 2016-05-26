"""
Sample.ex.py
"""
a = 1
b = 2

# Don't try negation of positive condition
if not a is b:
    print("No. This is wrong")

# Check inline negation in condition
if a is not b:
    print("Yes. You got it right")
