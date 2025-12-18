#1. Even number from a list
def get_even_numbers(lst):
    return[x for x in lst if x % 2 == 0]
print("Even numbers:", get_even_numbers([1,2,3,4,5,6]))

#2. Character count in a string

def char_count(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count
print("Character count:", char_count("hello"))

#3. check if a number is a palindrome
def is_palindrome(num):
    s = str(num)
    return s == s[::-1]
print("Is 121 palindrome?", is_palindrome(121))
print("Is 123 palindrome?", is_palindrome(123))

#4. Average of variable-length arguments
def average(*agrs):
    return sum(args) / len(args) if args else 0
print("Average:", average(10, 20, 30))

#5. Common elements from two lists (no set operations)

def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result
print("Common elements:", common_elements([1,2,3,4], [3,4,5,6]))
