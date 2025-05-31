def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    # Handle the rotation
    D = D % len(ARR)  # Handle cases where D is larger than the size of the list
    return ARR[D:] + ARR[:D]

# Helper function to display the result (for debugging)
def display_result(ARR, D):
    print(rotate_left(ARR, D))

ARR = [1, 2, 3, 4, 5]
D = 2
display_result(ARR, D)  # Output should be [3, 4, 5, 1, 2]
