# Define the binary search function that takes a list 'arr' and a target element 'target'
def binary_search(arr, target):
    # Initialize 'left' as the first index of the list and 'right' as the last index of the list
    left, right = 0, len(arr) - 1

    # Keep searching until 'left' becomes greater than 'right'
    while left <= right:
        # Calculate the index of the middle element in the current search range
        mid = (left + right) // 2

        # If the middle element is equal to the target, we found the element
        if arr[mid] == target:
            return mid

        # If the middle element is less than the target, discard the left half of the search range
        elif arr[mid] < target:
            left = mid + 1

        # If the middle element is greater than the target, discard the right half of the search range
        else:
            right = mid - 1

    # If the target element is not found in the list, return -1
    return -1

# Example usage:
if __name__ == "__main__":
    # Take the list as input from the user
    input_list = input("Enter a list of space-separated numbers: ")
    # Convert the input string into a list of integers
    unsorted_list = [int(x) for x in input_list.split()]

    # Take the target element as input from the user
    target_element = int(input("Enter the target element to search: "))

    # Sort the list using Python's built-in sorted() function
    sorted_list = sorted(unsorted_list)
    # Print the sorted list
    print("Sorted list:", sorted_list)

    # Perform binary search on the sorted list and get the index of the target element
    index = binary_search(sorted_list, target_element)

    # If the index is not -1, the target element is found in the list
    if index != -1:
        print(f"Element {target_element} found at index {index}.")
    # If the index is -1, the target element is not in the list
    else:
        print(f"Element {target_element} not found in the list.")
