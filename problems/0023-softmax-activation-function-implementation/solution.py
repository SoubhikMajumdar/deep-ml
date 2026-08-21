import numpy as np

def softmax(scores: list[float]) -> list[float]:
    exp_scores = np.exp(scores - np.max(scores)) # subtract max of scores to prevent overflow, mathematically same in the end
    return (exp_scores / np.sum(exp_scores)).tolist()
