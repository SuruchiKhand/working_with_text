import numpy as np

data = [
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
]


def find_nearest_pair(data):
    # Get the numbe of lines(rows) in the data
    N = len(data)

    # Create an empty 20 array to store distances, using float type
    dist = np.empty((N, N), dtype=float)

    # Calculate Manhattan distance for every pair of lines
    for i in range(N):
        for j in range(N):
            if i == j:
                # Set diagonal elements to infinity to avoid self-comparison
                dist[i, j] = np.inf
            else:
                # Calculate Manhattan distance between line i and line j
                distance = 0
                for k in range(len(data[i])):
                    distance += abs(data[i][k] - data[j][k])
                dist[i, j] = distance
    print(np.unravel_index(np.argmin(dist), dist.shape))


find_nearest_pair(data)
