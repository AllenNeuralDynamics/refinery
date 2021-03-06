from refinery.javahelpers import imglib2

import numpy as np


def bbox(points):
    """
    corners of 3D bounding box of input points
    [xmin xmax]
    [ymin ymax]
    [zmin zmax]
    """
    return np.min(points, axis=0), np.max(points, axis=0)


def chunk_center(point, side_lengths):
    """chunk from center point"""
    center = np.array(point)
    side_lengths = np.array(side_lengths)
    origin = np.ceil(center - side_lengths / 2.0)
    corner = origin + side_lengths
    origin = np.round(origin).astype(int)
    corner = np.round(corner).astype(int)
    return _minmax_to_interval(origin, corner)


def chunk_corners_padded(p, q, pad):
    """padded chunk from 2 corner points, where padding
    is generated by dragging the origin and opposite corners away from each other"""
    return _minmax_to_interval(
        np.array(p, dtype=int) - np.array(pad, dtype=int),
        np.array(q, dtype=int) + np.array(pad, dtype=int))


def _minmax_to_interval(interval_min, interval_max):
    return imglib2.Intervals.createMinMax(
        interval_min[0], interval_min[1], interval_min[2],
        interval_max[0], interval_max[1], interval_max[2])
