import numpy as np

def zero_pad_image(img, pad_width):
    if not isinstance(pad_width, int) or pad_width < 0:
        return -1

    arr = np.asarray(img)

    if arr.ndim != 2:
        return -1

    rows, cols = arr.shape

    padded = np.zeros(
        (rows + 2 * pad_width, cols + 2 * pad_width),
        dtype=int
    )

    padded[
        pad_width:pad_width + rows,
        pad_width:pad_width + cols
    ] = arr

    return padded.tolist()


'''
import numpy as np

def zero_pad_image(img, pad_width):
    """
    Add zero padding around a grayscale image.
    
    Args:
        img: 2D list or numpy array of pixel values
        pad_width: integer number of pixels to pad on each side
    
    Returns:
        Padded image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Validate pad_width
    if not isinstance(pad_width, (int, np.integer)) or pad_width < 0:
        return -1

    # Convert input to numpy array
    try:
        arr = np.asarray(img)
    except Exception:
        return -1

    # Must be a 2D grayscale image
    if arr.ndim != 2:
        return -1

    # Ensure pixel values are numeric
    if not np.issubdtype(arr.dtype, np.number):
        return -1

    # Add zero padding
    padded = np.pad(
        arr,
        pad_width=((pad_width, pad_width), (pad_width, pad_width)),
        mode="constant",
        constant_values=0
    )

    # Return as a 2D list of integers
    return padded.astype(int).tolist()

'''