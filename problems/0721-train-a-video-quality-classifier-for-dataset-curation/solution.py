import numpy as np

def curate_videos(train_features, train_labels, test_features):
    """
    Train a linear video quality classifier and predict keep/discard for test videos.

    Args:
        train_features: array-like of shape (N, D)
        train_labels: array-like of shape (N,), values in {0, 1}
        test_features: array-like of shape (M, D)

    Returns:
        list[int]: predictions of length M (1 = keep, 0 = discard)
    """
    # Your code here
    X_train = np.asarray(train_features, dtype=float)
    y_train = np.asarray(train_labels)
    X_test = np.asarray(test_features, dtype=float)

    # Separate the two classes
    X0 = X_train[y_train == 0]
    X1 = X_train[y_train == 1]

    # Class means
    mean0 = np.mean(X0, axis=0)
    mean1 = np.mean(X1, axis=0)

    # Within-class scatter matrices
    centered0 = X0 - mean0
    centered1 = X1 - mean1

    S0 = centered0.T @ centered0
    S1 = centered1.T @ centered1
    Sw = S0 + S1

    # Fisher projection direction:
    # w = Sw^(-1)(mean1 - mean0)
    # pinv handles singular within-class scatter robustly.
    w = np.linalg.pinv(Sw) @ (mean1 - mean0)

    # Project the two class means
    projected_mean0 = mean0 @ w
    projected_mean1 = mean1 @ w

    # Midpoint decision threshold
    threshold = (projected_mean0 + projected_mean1) / 2.0

    # Project and classify test videos
    test_projections = X_test @ w

    return (test_projections > threshold).astype(int).tolist()