import numpy as np
def calculate_brightness(img):
    if img is None:
        return -1
    try:
        img = np.array(img)
    except (ValueError, TypeError):
        return -1

    # Must be a non-empty 2D matrix
    if img.size == 0 or img.ndim != 2:
        return -1

    total = 0.0
    height, width = img.shape
    for row in range(height):
        for col in range(width):
            pixel = img[row, col]
            try:
                if 0 <= pixel <= 255:
                    total += pixel
                else:
                    return -1
            except TypeError:
                return -1
    return round(total / img.size, 2)