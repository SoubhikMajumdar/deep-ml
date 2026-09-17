import numpy as np

def compute_psnr(original: np.ndarray, reconstructed: np.ndarray,
                 max_pixel_value: float) -> float:
    """
    Compute the Peak Signal-to-Noise Ratio between two images.
    """
    if np.array_equal(original, reconstructed):
        return float("inf")

    original = original.astype(np.float64)
    reconstructed = reconstructed.astype(np.float64)

    mse = np.mean((original - reconstructed) ** 2)

    psnr = 10 * np.log10((max_pixel_value ** 2) / mse)

    return float(psnr)