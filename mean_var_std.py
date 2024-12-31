import numpy as np

def calculate(list):
    # check if the input list has 9 elements
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        # convert the list to a 3x3 array
        matrix = np.array(list).reshape(3, 3)

    mean = [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist()),
            (matrix.flatten().mean())]

    var = [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()),
           (matrix.flatten().var())]

    std = [(matrix.std(axis=0).tolist()), (matrix.std(axis=1).tolist()),
           (matrix.flatten().std())]

    max = [(matrix.max(axis=0).tolist()), (matrix.max(axis=1).tolist()),
           (matrix.flatten().max())]

    min = [(matrix.min(axis=0).tolist()), (matrix.min(axis=1).tolist()),
           (matrix.flatten().min())]

    sum = [(matrix.sum(axis=0).tolist()), (matrix.sum(axis=1).tolist()),
           (matrix.flatten().sum())]

    # create a dictionary to store the calculations
    calculations = {
        "mean": mean,
        "variance": var,
        "standard deviation": std,
        "max": max,
        "min": min,
        "sum": sum,
    }
    return calculations