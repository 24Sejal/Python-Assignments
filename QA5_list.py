import copy

original = [[1,2],[3,4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print("Original: ", original)
print("Shallow copy: ", shallow)
print("Deep copy: ", deep)