import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    r0 = np.random.rand(data.shape[0])
    rn = r0
    for i in range(num_steps):
        tmp = data.dot(rn)
        rn = tmp / np.linalg.norm(tmp)

    mu = float(rn.T.dot(data.dot(rn)) / (rn.T.dot(rn)))
    return mu, rn