# Practical 10 – Binary Search (Python)

## 👨‍🏫 Aim
To implement the Binary Search algorithm in Python.

---

## 📌 Introduction
Binary Search is a searching algorithm used to find an element in a **sorted array**.  
It works on the principle of **divide and conquer**, repeatedly dividing the search interval in half.

Binary Search is much faster than Linear Search for large datasets.

---

## 📘 Algorithm

1. Start with two pointers:  
   - `left = 0`  
   - `right = n - 1`

2. Find the middle index:  
   `mid = left + (right - left) // 2`

3. Compare middle element with the target:
   - If `arr[mid] == target`: return the index  
   - If `arr[mid] < target`: search in the right half  
   - If `arr[mid] > target`: search in the left half  

4. Repeat until `left <= right`.

5. If not found, return `-1`.

---

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

Binary Search is efficient because it cuts down the search space by half each time.

---

## 🧪 Python Code

```python
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
