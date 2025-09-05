def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # Calculate middle index

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # If target is not found in the array
    return -1

# Example Usage:
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
search_target = 23

result_index = binary_search(sorted_list, search_target)

if result_index != -1:
    print(f"Element {search_target} found at index {result_index}")
else:
    print(f"Element {search_target} not found in the list")

search_target_not_found = 100
result_not_found = binary_search(sorted_list, search_target_not_found)
if result_not_found != -1:
    print(f"Element {search_target_not_found} found at index {result_not_found}")
else:
    print(f"Element {search_target_not_found} not found in the list")
