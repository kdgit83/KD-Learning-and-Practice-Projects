def insertion_sort(lst: list) -> list:
    """
    Insertion Sort:
    The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array
    to hold values that are not sorted yet.

    Insertion Sort Algorithm:
    You are given a list of integers. Write a Python function to sort the list in ascending order using the Insertion
    Sort algorithm. Insertion Sort works by building a sorted section of the list, one element at a time, by inserting
    each new element into its proper position within the already sorted section.

    How it works:
        1) Take the first value from the unsorted part of the array.
        2) Move the value into the correct place in the sorted part of the array.
        3) Go through the unsorted part of the array again as many times as there are values.

    Reference Links:
    https://www.w3schools.com/dsa/dsa_algo_insertionsort.php
    https://www.geeksforgeeks.org/insertion-sort-algorithm/

    Time Complexity
        Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
        Average case: O(n2), If the list is randomly ordered
        Worst case: O(n2), If the list is in reverse order
    Space Complexity
        Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.

    Advantages and Disadvantages of Insertion Sort
    Advantages
    Simple and easy to implement.
    Stable sorting algorithm.
    Efficient for small lists and nearly sorted lists.
    Space-efficient as it is an in-place algorithm.
    Adoptive. the number of inversions is directly proportional to number of swaps. For example, no swapping happens
    for a sorted array, and it takes O(n) time only.
    Disadvantages
    Inefficient for large lists.
    Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.

    Parameters:
    lst (List of integers): The list to be sorted.

    Returns:
    A list of integers sorted in ascending order.

    Example:
    Input: lst = [12, 11, 13, 5, 6]
    Output: [5, 6, 11, 12, 13]

    Input: lst = [31, 41, 59, 26, 41, 58]
    Output: [26, 31, 41, 41, 58, 59]
    """
    n = len(lst)

    for i in range(1, n):
        current_card = lst[i]
        correct_position = i - 1

        while correct_position >= 0:
            if lst[correct_position] < current_card:
                break
            else:
                lst[correct_position + 1] = lst[correct_position]
                correct_position -= 1
            lst[correct_position + 1] = current_card

    return lst

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print(arr)
