
# This program defines a method that takes in two strings and returns true if the second string is substring of the first, and false otherwise

def substring(str, substr):
    if len(substr) < 1:
        return True

    for i in range(len(str)):
        str_i, sub_j = i, 0
        while str_i < len(str) and sub_j < len(substr) and str[str_i] == substr[sub_j]:
            str_i += 1
            sub_j += 1
        if sub_j == len(substr):
            return True 
    return False

print(substring("Hello", "ell"))
