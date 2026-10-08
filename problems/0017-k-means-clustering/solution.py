import numpy as np


def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:
    """
    Perform k-means clustering.

    Returns:
        Final centroids rounded to four decimal places.
    """

    points_array = np.asarray(points, dtype=float)
    centroids = np.asarray(initial_centroids, dtype=float)

    if len(points_array) == 0:
        return []

    if k <= 0:
        raise ValueError("k must be positive")

    if len(initial_centroids) != k:
        raise ValueError("Number of initial centroids must equal k")

    if points_array.ndim != 2 or centroids.ndim != 2:
        raise ValueError("Points and centroids must be 2D arrays")

    if points_array.shape[1] != centroids.shape[1]:
        raise ValueError(
            "Points and centroids must have the same dimensionality"
        )

    for _ in range(max_iterations):

        # Shape:
        # points_array[:, None, :] -> (number_of_points, 1, dimensions)
        # centroids[None, :, :]    -> (1, k, dimensions)
        differences = (
            points_array[:, np.newaxis, :]
            - centroids[np.newaxis, :, :]
        )

        # Distance from every point to every centroid
        # Shape: (number_of_points, k)
        distances = np.linalg.norm(differences, axis=2)

        # Closest centroid for every point
        # Shape: (number_of_points,)
        labels = np.argmin(distances, axis=1)

        new_centroids = np.copy(centroids)

        # Recompute each centroid
        for cluster_index in range(k):
            cluster_points = points_array[labels == cluster_index]

            # If no points belong to this cluster, keep its old centroid
            if len(cluster_points) > 0:
                new_centroids[cluster_index] = np.mean(
                    cluster_points,
                    axis=0
                )

        # Stop if centroids no longer change
        if np.allclose(centroids, new_centroids):
            centroids = new_centroids
            break

        centroids = new_centroids

    # Convert NumPy rows into tuples rounded to four decimal places
    final_centroids = [
        tuple(round(float(value), 4) for value in centroid)
        for centroid in centroids
    ]

    return final_centroids