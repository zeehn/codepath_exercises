# This program reverses a given string in O(n) time complexity.

def reverse_string(input_str):
    arr = list(input_str)
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
    return "".join(arr)

str = "Hello"

print(reverse_string(str))
