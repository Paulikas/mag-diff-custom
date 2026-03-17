'''
File for functions that calculate diff of 2 given point clounds.
'''

import os
from typing import List

from tqdm import tqdm
from config import MODEL_ITER
from plyfile import PlyData
import numpy as np
import pandas as pd

from utils.logger import get_logger
logger = get_logger(__name__)

# utilites

def prep_path_3DGS(model_path: str, iter = MODEL_ITER[0]):
    '''
    Deprecated
    '''
    return os.path.join(model_path, "point_cloud","iteration_" + str(iter),"scene_point_cloud.ply")

def save_np_to_csv(nparray: np.ndarray, filename: str, columns: List = [], path = ""):
    '''
    Saves ply file data to csv.

    Should check if output folder exits and created if needed. Future TODO.
    
    :param nparray: Description
    :type nparray: np.ndarray
    :param filename: Description
    :type filename: str
    :param columns: Description
    :type columns: List
    :param path: Description
    '''
    with_columns = True
    if len(columns) == 0:
        with_columns = False

    path_to_save = os.path.join(path, filename + ".csv")
    print(f"path where file {filename} will be save: {path_to_save}")

    if with_columns == True:
        # writes to pandas dataframe, that allows collumn
        print("Writing data to csv with colums")

        df = pd.DataFrame(nparray, columns=columns)
        df.to_csv(path_to_save)

    else:
        # writes it to csv out of the box using numpy    
        nparray.tofile(path_to_save, sep=',')

def get_plydata(path):
    return PlyData.read(path)


# calculation part. Main function get_diff

def check_position(pos1: List, pos2: List, error_margin:float = 0.0):
    '''
    DEPRECATED: Now handled natively by scipy.spatial.cKDTree in get_diff
    Check the x, y, z koordinates. Not including nx, ny, nz data.
    '''
    # allowed ranges
    # for x
    allowed_x_max = pos1[0] + error_margin
    allowed_x_min = pos1[0] - error_margin
    check_res_x = False

    # for y
    allowed_y_max = pos1[1] + error_margin
    allowed_y_min = pos1[1] - error_margin
    check_res_y = False

    # for z
    allowed_z_max = pos1[2] + error_margin
    allowed_z_min = pos1[2] - error_margin
    check_res_z = False

    if pos2[0] >= allowed_x_min and pos2[0] <= allowed_x_max:
        # print(f"x matches at {pos1[0]} and {pos2[0]}")
        check_res_x = True

    if pos2[1] >= allowed_y_min and pos2[1] <= allowed_y_max:
        # print(f"y matches at {pos1[1]} and {pos2[1]}")
        check_res_y = True

    if pos2[2] >= allowed_z_min and pos2[2] <= allowed_z_max:
        # print(f"z matches at {pos1[2]} and {pos2[2]}")
        check_res_z = True

    if check_res_x and check_res_y and check_res_z:
        return True
    else:
        return False

def check_data(point1: List, point2: List, type: str = 'blender', error_margin: float = 0.0):
    '''
    DEPRECATED: Now handled natively by scipy.spatial.cKDTree in get_diff
    Returns True if points are identical within error margin
    Return False if point are not similar
    '''
    check_result = False

    for i in range(len(point1)):
        
        allowed_max = point1[i] + error_margin
        allowed_min = point1[i] - error_margin

        if point2[i] >= allowed_min and point2[i] <= allowed_max:
            check_result = True
        else:
            check_result = False
            break
        
    return check_result

    

def get_diff(model1: np.ndarray, model2: np.ndarray, type: str = 'blender', error_margin: float = 0.0): # -> np.ndarray:
    '''    
    :param type: possible values ['blender', '3DGS']
    '''
    if len(model1) > len(model2):
        benchmark = model2
        change = model1
    else:
        benchmark = model1
        change = model2

    logger.info(f"Starting comparison of {len(change)} points with {len(benchmark)} points")

    from scipy.spatial import cKDTree

    # Build a KD-Tree on all spatial attributes of the benchmark array
    # This allows us to search across xyz, normals, colors, etc. simultaneously
    tree = cKDTree(benchmark)

    # Query the KDTree for the nearest neighbor of each point in 'change'
    # We use p=np.inf to apply the same error_margin across all attributes (Chebyshev distance)
    # The [0] element returned by query() is the distance array (the second is the indices)
    distances, _ = tree.query(change, p=np.inf)

    # Filter the points in 'change' whose nearest match in 'benchmark'
    # is strictly outside of the allowed error_margin.
    logger.info(f"Using value of error margins as: {error_margin}")
    is_different = distances > error_margin
    
    # We slice out just the points that don't match our criteria
    difference = change[is_different]

    logger.info(f"Found {len(difference)} points that are not in the other model")           
    return difference
    