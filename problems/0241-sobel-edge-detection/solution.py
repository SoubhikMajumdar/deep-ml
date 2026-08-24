import numpy as np

def sobel_edge_detection(image):
    """
    Apply Sobel edge detection to a grayscale image.

    Returns:
        Edge magnitude image as a 2D list with integer values (0–255),
        or -1 if the input is invalid.
    """

    # Convert and validate input
    try:
        image = np.asarray(image, dtype=float)
    except (TypeError, ValueError):
        return -1

    if (
        image.ndim != 2
        or image.size == 0
        or image.shape[0] < 3
        or image.shape[1] < 3
        or not np.all(np.isfinite(image))
        or np.any(image < 0)
        or np.any(image > 255)
    ):
        return -1

    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=float)

    sobel_y = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ], dtype=float)

    height, width = image.shape
    magnitudes = np.zeros((height - 2, width - 2), dtype=float)

    # Valid convolution: only locations with a complete 3x3 region
    for row in range(height - 2):
        for col in range(width - 2):
            region = image[row:row + 3, col:col + 3]

            gradient_x = np.sum(region * sobel_x)
            gradient_y = np.sum(region * sobel_y)

            magnitudes[row, col] = np.sqrt(
                gradient_x**2 + gradient_y**2
            )

    # Normalize globally based on the strongest edge
    max_magnitude = np.max(magnitudes)

    if max_magnitude > 0:
        magnitudes = magnitudes / max_magnitude * 255

    return magnitudes.astype(int).tolist()