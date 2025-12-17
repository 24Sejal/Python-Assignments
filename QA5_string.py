s = "Hello"

try:
    s[0] = "h"
except TypeError as e:
    print("Error:", e)