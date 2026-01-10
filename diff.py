'''
File for functions that calculate diff of 2 given point clounds.
'''

import os
from typing import List
from config import MODEL_ITER
from plyfile import PlyData
import numpy as np
import pandas as pd

def get_diff(model1, model2):
    pass

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