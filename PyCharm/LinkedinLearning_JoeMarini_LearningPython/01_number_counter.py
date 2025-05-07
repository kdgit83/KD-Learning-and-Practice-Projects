def count_numbers(which: str, numbers: list[int]) -> int:
    # Your code goes here
    count = 0
    if which.lower() == "even":
        for i in numbers:
            if i%2 == 0:
                count += 1
        return count
    elif which.lower() == "odd":
        for i in numbers:
            if i%2 != 0:
                count += 1
        return count
    return -1

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]
for i, j in [("even", numbers), ("odd", numbers), ("Blarg", numbers)]:
    print(f"{i} count: {count_numbers(i, j)}")
