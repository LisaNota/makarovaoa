from time import perf_counter

import numpy as np
from numpy.typing import NDArray
from functools import cmp_to_key

from src.plotting import plot_points

def compare(x: list, y: list) -> int:
    # sort the vertices first by x-coordinate, then by y-coordinate
    if (x[0] < y[0]) or (x[0] == y[0] and x[1] < y[1]):
        return -1
    elif (x[0] == y[0] and x[1] == y[1]):
        return 0
    return 1

def rotate(x: list, y: list, z: list) -> bool:
    # this function determines which side of the vector XY is the point Z
    if np.sign((z[0]-y[0])*(y[1]-x[1]) - (z[1]-y[1])*(y[0]-x[0])) >= 0:
        return True
    return False

def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    clockwise_sorted_ch = []

    points = sorted(points, key=cmp_to_key(compare))
    clockwise_sorted_ch.append(points[0])
    clockwise_sorted_ch.append(points[1])

    for point in points[2::]:
        while (len(clockwise_sorted_ch) > 1) and (rotate(clockwise_sorted_ch[-2], clockwise_sorted_ch[-1], point)):
            clockwise_sorted_ch.pop()
        clockwise_sorted_ch.append(point)
        
    return np.array(clockwise_sorted_ch + clockwise_sorted_ch[-2::-1])


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"practicum_5/homework/points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
