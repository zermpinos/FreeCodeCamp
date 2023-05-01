import numpy as np


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array = np.array(numbers).reshape(3, 3)

    return {
        # axis equal to 0 means column and 1 means row, then the flattened matrix
        'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean()],
        'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var()],
        'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std()],
        'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max()],
        'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min()],
        'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum()]
    }
