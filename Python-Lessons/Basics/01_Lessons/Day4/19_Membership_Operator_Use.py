# ---Membership operators use with strings---

# in Operator.
s = "I love programming"
if "love" in s:
    print("Akshat loves programming.")
    print("love" in s) # Prints True because the substring "love" does exist in the string s.

# not in Operator.
if "hate" not in s:
    print("Akshat still loves programming.")
    print("hate" not in s) # Prints True because the substring "hate" does not exist in string s.