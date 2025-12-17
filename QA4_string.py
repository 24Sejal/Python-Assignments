s = input("Enter a string: ")
freq ={}

for i in s:
    freq[i] = freq.get(i,0)+1

for key, value in freq.items():
    print(key,"->",value)