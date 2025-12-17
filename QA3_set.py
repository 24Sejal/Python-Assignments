a = {1,2}
b = {1,2,3,4}

is_subset = True
for i in a:
    if i not in b:
        is_subset = False
        break

print("Subset:", is_subset)