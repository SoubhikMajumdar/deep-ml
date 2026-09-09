import numpy as np

def flip_image(image, direction):
    """
    Flip an image horizontally or vertically.
    
    Args:
        image: 2D or 3D list/array representing a grayscale or RGB image
        direction: string, either 'horizontal' or 'vertical'
    
    Returns:
        Flipped image as a nested list, or -1 if input is invalid
    """
    try:
        arr = np.asarray(image)

        if arr.ndim not in (2,3):
            return -1

        if arr.ndim == 3 and arr.shape[2] != 3:
            return -1

        if direction == 'vertical':
            flipped = np.flip(arr, axis = 0)
        elif direction == 'horizontal':
            flipped = np.flip(arr, axis = 1)
        else:
            return -1

        return flipped.tolist()

    except (TypeError, ValueError):
        return -1
