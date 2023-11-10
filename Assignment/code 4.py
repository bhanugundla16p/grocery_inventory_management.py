def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr  # Add a return statement to return the sorted array

# Get input from the user
input_str = input("Enter a list of numbers separated by commas: ")
input_list = [int(x) for x in input_str.split(',')]

# Perform merge sort
sorted_list = merge_sort(input_list)

# Print the sorted result
print(f"The sorted list is: {sorted_list}")
