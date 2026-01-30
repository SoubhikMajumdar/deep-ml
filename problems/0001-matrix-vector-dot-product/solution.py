import numpy as np

def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Check dimension compatibility
    if not a or len(a[0]) != len(b):
        return -1

    # Convert to NumPy arrays
    matrix = np.array(a)
    vector = np.array(b)

    # Compute dot product
    result = matrix.dot(vector)

    # Convert result back to a Python list
    return result.tolist()
