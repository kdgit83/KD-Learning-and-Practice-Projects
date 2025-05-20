def bubble_sort(arr: list) -> list | None:
    """
    Bubble Sort:
    Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

    Bubble Sort Algorithm:
    You are given a list of integers. Write a Python function to sort the list in ascending order using the Bubble Sort
    algorithm. Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in
    the wrong order. The process is repeated until the list is sorted.

    How it works:
        1) Go through the array, one value at a time.
        2) For each value, compare the value with the next value.
        3) If the value is higher than the next one, swap the values so that the highest value comes last.
        4) Go through the array as many times as there are values in the array.

    Reference Links:
    https://www.w3schools.com/dsa/dsa_algo_bubblesort.php
    https://www.geeksforgeeks.org/bubble-sort-algorithm/

    Complexity Analysis of Bubble Sort:
    Time Complexity: O(n2)
    Auxiliary Space: O(1)

    Advantages of Bubble Sort:
    Bubble sort is easy to understand and implement.
    It does not require any additional memory space.

    Disadvantages of Bubble Sort:
    Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.
    Bubble sort has almost no or limited real world applications. It is mostly used in academics mostly.

    Parameters:
    lst (List of integers): The list to be sorted.

    Returns:
    A list of integers sorted in ascending order.

    Example:
    Input: lst = [64, 34, 25, 12, 22, 11, 90]
    Output: [11, 12, 22, 25, 34, 64, 90]

    Input: lst = [5, 1, 4, 2, 8]
    Output: [1, 2, 4, 5, 8]
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        swapped = False
        # Last i elements are already in place
        for j in range(n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
