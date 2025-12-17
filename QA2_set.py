s1 = {1,2,3,4}
s2 = {3,4,5,6}

common = s1 & s2
s1 = s1 - common
s2 = s2 - common

print("Set 1:", s1)
print("Set 2:", s2)