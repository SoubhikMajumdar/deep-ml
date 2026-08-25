import numpy as np

def temporal_aggregate(features, k: int):
    """
    Aggregate frame features by averaging every k consecutive frames.

    Args:
        features: 2D array-like of shape (num_frames, feature_dim)
        k: aggregation factor (positive int)

    Returns:
        Nested list of shape (num_frames // k, feature_dim)
    """

    features = np.asarray(features)

    num_complete = len(features) // k
    trimmed = features[:num_complete*k]
    if num_complete == 0:
        return []

    aggregated = trimmed.reshape(num_complete, k, -1).mean(axis=1)
    return aggregated.tolist()

    