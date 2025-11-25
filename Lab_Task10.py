# Binary Search Implementation – Practical 10

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# main program
if __name__ == "__main__":
    n = int(input("Enter size of array: "))
    arr = []

    print("Enter elements in sorted order:")
    for _ in range(n):
        arr.append(int(input()))

    target = int(input("Enter element to search: "))

    result = binary_search(arr, target)

    if result == -1:
        print("Element NOT FOUND in array.")
    else:
        print(f"Element found at index: {result}")
