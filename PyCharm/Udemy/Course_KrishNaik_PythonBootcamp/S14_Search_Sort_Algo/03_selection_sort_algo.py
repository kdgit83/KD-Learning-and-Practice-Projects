def selection_sort(lst):
    """
    Selection Sort:
    The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

    Selection Sort Algorithm:
    You are given a list of integers. Write a Python function to sort the list in ascending order using the Selection
    Sort algorithm. Selection Sort works by repeatedly finding the minimum element from the unsorted part of the list
    and swapping it with the first element of the unsorted part.

    How it works:
        1) Go through the array to find the lowest value.
        2) Move the lowest value to the front of the unsorted part of the array.
        3) Go through the array again as many times as there are values in the array.

    Reference Links:
    https://www.w3schools.com/dsa/dsa_algo_selectionsort.php
    https://www.geeksforgeeks.org/selection-sort-algorithm-2/

    Complexity Analysis of Selection Sort:
    Time Complexity: O(n2)
    Auxiliary Space: O(1)

    Advantages of Selection Sort:
    Selection sort is easy to understand and implement.
    Requires only a constant O(1) extra memory space.

    Disadvantages of Selection Sort:
    Selection sort has a time complexity of O(n^2) makes it slower compared to algorithms like Quick Sort or Merge Sort.
    Does not maintain the relative order of equal elements which means it is not stable.

    Parameters:
    lst (List of integers): The list to be sorted.

    Returns:
    A list of integers sorted in ascending order.

    Example:
    Input: lst = [64, 25, 12, 22, 11]
    Output: [11, 12, 22, 25, 64]

    Input: lst = [29, 10, 14, 37, 13]
    Output: [10, 13, 14, 29, 37]
    """
    # Your code goes here
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    print("Original array: ", end="")
    print(arr)

    selection_sort(arr)

    print("Sorted array: ", end="")
    print(arr)
