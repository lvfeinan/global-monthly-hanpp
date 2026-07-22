"""Grid alignment and resampling helpers.

Functions for aligning different-resolution rasters to the target 0.1-degree grid,
reprojection, and spatial resampling utilities.
"""

import numpy as np
import xarray as xr
import rioxarray


def create_target_grid(target_res=0.1):
    """Create a target grid where cell values are true geodetic area (m^2).

    Uses the WGS84 ellipsoid to compute the area of each 0.1-degree cell,
    varying by latitude. All cells in the same row share the same area.

    Parameters
    ----------
    target_res : float
        Grid resolution in degrees (default 0.1 degree).

    Returns
    -------
    xr.DataArray
        Shape (y, x) with values = cell area in m^2, CRS = EPSG:4326.
    """
    from pyproj import Geod

    half_res = target_res / 2
    y = np.arange(-60 + half_res, 80, target_res)
    x = np.arange(-180 + half_res, 180, target_res)

    geod = Geod(ellps='WGS84')
    area_1d = np.empty(len(y))
    for i, y_c in enumerate(y):
        poly_area, _ = geod.polygon_area_perimeter(
            [0, target_res, target_res, 0, 0],
            [y_c - half_res, y_c - half_res,
             y_c + half_res, y_c + half_res, y_c - half_res],
        )
        area_1d[i] = abs(poly_area)

    area_grid = np.broadcast_to(area_1d[:, np.newaxis], (len(y), len(x)))

    return (
        xr.DataArray(area_grid, dims=['y', 'x'], coords={'y': y, 'x': x})
        .rio.write_crs("EPSG:4326")
    )
