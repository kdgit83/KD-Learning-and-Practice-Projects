def area_of_rectangle(length: float, breadth: float) -> float:
    """
    Function to calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    breadth (float): The breadth of the rectangle.

    Returns:
    float: The area of the rectangle.

    Problem Description:
    You are given the length and breadth of a rectangle. Your task is to compute and return the area of the rectangle.
    Formula:
    To calculate the area of a rectangle: Area=length×breadth
    Input:
    Two floating-point numbers, length and breadth, representing the dimensions of the rectangle.
    Output:
    A floating-point number representing the area of the rectangle.
    Example:
    Input: length = 5, breadth = 3
    Output: 15.0
    Input: length = 7.5, breadth = 2.4
    Output: 18.0
    """
    # Your code here
    return float(length * breadth)

for i, j in [(5,3), (7.5, 2.4), (50.50, 28)]:
    print(area_of_rectangle(i, j))
