def sum_array(arr):
    
    if len(arr) == 0:
        return 0

    return arr[0] + sum_array(arr[1:])

def find_largest(arr):
    
    if len(arr) == 0:
        raise ValueError("Array must contain at least one number")

    if len(arr) == 1:
        return arr[0]

    largest_rest = find_largest(arr[1:])

    if arr[0] > largest_rest:
        return arr[0]
    else:
        return largest_rest

def count_number(arr, target):
  
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)


print("===== RECURSIVE ARRAY TOOLKIT =====")


print("\n1. SUM THE ARRAY")
print("Empty array:", sum_array([]))
print("One number:", sum_array([5]))
print("Multiple numbers:", sum_array([10, 20, 30]))
print("Positive and negative:", sum_array([5, -2, 8, -1]))

print("\n2. FIND THE LARGEST NUMBER")
print("One number:", find_largest([7]))
print("Largest at beginning:", find_largest([20, 5, 10, 15]))
print("Largest at end:", find_largest([3, 8, 12, 25]))
print("Negative numbers:", find_largest([-10, -3, -20, -5]))

print("\n3. COUNT A CHOSEN NUMBER")
print("Empty array:", count_number([], 5))
print("Several occurrences:", count_number([2, 5, 2, 8, 2, 5], 2))
print("Number not found:", count_number([1, 3, 4, 6], 9))

print("\n===== END OF TESTING =====")