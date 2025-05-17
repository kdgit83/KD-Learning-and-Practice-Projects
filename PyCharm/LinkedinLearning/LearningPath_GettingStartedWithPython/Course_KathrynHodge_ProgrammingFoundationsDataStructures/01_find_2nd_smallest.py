def find_second_smallest(num_list: list) -> int | None:
    if len(num_list) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')
    for num in num_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest

print(find_second_smallest([5, 8,  3, 2, 6]))
