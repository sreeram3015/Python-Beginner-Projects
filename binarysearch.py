def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return sort(left) + middle + sort(right)

# Example usage:
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = sort(unsorted_list)
    print("Sorted list:", sorted_list)

    target_element = 22
    index = binary_search(sorted_list, target_element)
    if index != -1:
        print(f"Element {target_element} found at index {index}.")
    else:
        print(f"Element {target_element} not found in the list.")
