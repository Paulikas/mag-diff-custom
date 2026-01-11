'''
File for functions that calculate diff of 2 given point clounds.
'''

import os
from typing import List
from config import MODEL_ITER
from plyfile import PlyData
import numpy as np
import pandas as pd

# utilites

def prep_path_3DGS(model_path: str, iter = MODEL_ITER[0]):
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

def load_ply_blender(path):
    plydata = get_plydata(path)

    # if there is no nx, ny, nz then the array is not fill with those columns
    columns = plydata.elements[0].properties

    check = False
    for i in columns:
        if i.name == "nx":
            check = True

    if check:  
        data = np.stack((np.asarray(plydata.elements[0]['x']),
                        np.asarray(plydata.elements[0]['y']),
                        np.asarray(plydata.elements[0]['z']),
                        np.asarray(plydata.elements[0]['nx']),
                        np.asarray(plydata.elements[0]['ny']),
                        np.asarray(plydata.elements[0]['nz']),
                        np.asarray(plydata.elements[0]['s']),
                        np.asarray(plydata.elements[0]['t'])
                        ), axis=1)
        
    else:
        data = np.stack((np.asarray(plydata.elements[0]['x']),
                        np.asarray(plydata.elements[0]['y']),
                        np.asarray(plydata.elements[0]['z']),
                        np.asarray(plydata.elements[0]['s']),
                        np.asarray(plydata.elements[0]['t'])
                        ), axis=1)

    return data

def load_ply_3DGS(path):
    '''
    Load ply from 3DGS file data to nparray
    
    :param path: to cloud point data, path must be fortamted by prep_path function
    '''
    plydata = get_plydata(path)

    data = np.stack((np.asarray(plydata.elements[0]["x"]),
                    np.asarray(plydata.elements[0]["y"]),
                    np.asarray(plydata.elements[0]["z"]),
                    np.asarray(plydata.elements[0]["nx"]),
                    np.asarray(plydata.elements[0]["ny"]),
                    np.asarray(plydata.elements[0]["nz"]),
                    np.asarray(plydata.elements[0]["f_dc_0"]),
                    np.asarray(plydata.elements[0]["f_dc_1"]),
                    np.asarray(plydata.elements[0]["f_dc_2"]),
                    np.asarray(plydata.elements[0]["f_rest_0"]),
                    np.asarray(plydata.elements[0]["f_rest_1"]),
                    np.asarray(plydata.elements[0]["f_rest_2"]),
                    np.asarray(plydata.elements[0]["f_rest_3"]),
                    np.asarray(plydata.elements[0]["f_rest_4"]),
                    np.asarray(plydata.elements[0]["f_rest_5"]),
                    np.asarray(plydata.elements[0]["f_rest_6"]),
                    np.asarray(plydata.elements[0]["f_rest_7"]),
                    np.asarray(plydata.elements[0]["f_rest_8"]),
                    np.asarray(plydata.elements[0]["f_rest_9"]),
                    np.asarray(plydata.elements[0]["f_rest_10"]),
                    np.asarray(plydata.elements[0]["f_rest_11"]),
                    np.asarray(plydata.elements[0]["f_rest_12"]),
                    np.asarray(plydata.elements[0]["f_rest_13"]),
                    np.asarray(plydata.elements[0]["f_rest_14"]),
                    np.asarray(plydata.elements[0]["f_rest_15"]),
                    np.asarray(plydata.elements[0]["f_rest_16"]),
                    np.asarray(plydata.elements[0]["f_rest_17"]),
                    np.asarray(plydata.elements[0]["f_rest_18"]),
                    np.asarray(plydata.elements[0]["f_rest_19"]),
                    np.asarray(plydata.elements[0]["f_rest_20"]),
                    np.asarray(plydata.elements[0]["f_rest_21"]),
                    np.asarray(plydata.elements[0]["f_rest_22"]),
                    np.asarray(plydata.elements[0]["f_rest_23"]),
                    np.asarray(plydata.elements[0]["f_rest_24"]),
                    np.asarray(plydata.elements[0]["f_rest_25"]),
                    np.asarray(plydata.elements[0]["f_rest_26"]),
                    np.asarray(plydata.elements[0]["f_rest_27"]),
                    np.asarray(plydata.elements[0]["f_rest_28"]),
                    np.asarray(plydata.elements[0]["f_rest_29"]),
                    np.asarray(plydata.elements[0]["f_rest_30"]),
                    np.asarray(plydata.elements[0]["f_rest_31"]),
                    np.asarray(plydata.elements[0]["f_rest_32"]),
                    np.asarray(plydata.elements[0]["f_rest_33"]),
                    np.asarray(plydata.elements[0]["f_rest_34"]),
                    np.asarray(plydata.elements[0]["f_rest_35"]),
                    np.asarray(plydata.elements[0]["f_rest_36"]),
                    np.asarray(plydata.elements[0]["f_rest_37"]),
                    np.asarray(plydata.elements[0]["f_rest_38"]),
                    np.asarray(plydata.elements[0]["f_rest_39"]),
                    np.asarray(plydata.elements[0]["f_rest_40"]),
                    np.asarray(plydata.elements[0]["f_rest_41"]),
                    np.asarray(plydata.elements[0]["f_rest_42"]),
                    np.asarray(plydata.elements[0]["f_rest_43"]),
                    np.asarray(plydata.elements[0]["f_rest_44"]),
                    np.asarray(plydata.elements[0]["opacity"]),
                    np.asarray(plydata.elements[0]["scale_0"]),
                    np.asarray(plydata.elements[0]["scale_1"]),
                    np.asarray(plydata.elements[0]["scale_2"]),
                    np.asarray(plydata.elements[0]["rot_0"]),
                    np.asarray(plydata.elements[0]["rot_1"]),
                    np.asarray(plydata.elements[0]["rot_2"]),
                    np.asarray(plydata.elements[0]["rot_3"])
                    ),  axis=1)

    return data

# calculation part. Main function get_diff

def check_position(pos1: List, pos2: List, error_margin:float = 0.0):
    '''
    DEPRECATED
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
        
    return check_result

    

def get_diff(model1: np.ndarray, model2:np.ndarray, type: str = 'blender', error_margin: float = 0.0): # -> np.ndarray:
    '''    
    :param type: passible values ['blender', '3DGS']
    '''
    difference = []
    is_match = False

    if len(model1) > len(model2):
        bendchmar = model2
        change = model1
    else:
        bendchmar = model1
        change = model2



    # a loop to move both models throu.
    # [0] = x, [1] = y, [2]= z
    for i in change:
        for j in bendchmar:

            is_match = False
            
            if check_position(i, j, error_margin=error_margin):
                if check_data(i, j, error_margin=error_margin):
                    is_match = True
                    break
                else:
                    # should here be the code to check if neighbors are not similar.
                    is_match = False
                    
                
                
        if is_match == False:
            difference.append(i)
        
                   
    return difference
    