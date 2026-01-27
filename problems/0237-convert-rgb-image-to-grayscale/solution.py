import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    try:
        # Convert to numpy array
        img = np.array(image)

        # Validate shape
        if img.ndim != 3 or img.shape[2] != 3:
            return -1

        # Validate pixel value range
        if not np.issubdtype(img.dtype, np.number):
            return -1
        if np.any(img < 0) or np.any(img > 255):
            return -1

        # Apply luminosity formula
        gray = (
            0.299 * img[:, :, 0] +
            0.587 * img[:, :, 1] +
            0.114 * img[:, :, 2]
        )

        # Convert to integers
        gray = gray.round()

        # Return as 2D list
        return gray.tolist()

   