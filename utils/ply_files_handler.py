from datetime import datetime
import os
import numpy as np
from plyfile import PlyData, PlyElement


def get_plydata(path):
    return PlyData.read(path)


def save_plydata(plydata, path):
    plydata.write(path)


def save_list_to_ply(data_list, path, cloud_type='blender'):
    """
    Saves a list of numpy arrays (representing point cloud points) to a PLY file.

    This function takes a list of numpy array objects, each representing a single point
    with its properties, converts them into a structured numpy array, and saves them
    to a PLY file using the plyfile library.

    It supports predefined 'blender' and '3DGS' formats found in the project.
    If the cloud_type is not recognized, it will attempt to assign generic
    property names based on the number of columns.

    Usage:
    - For Blender data (5 or 8 columns):
        save_list_to_ply(diff_list, 'output.ply', cloud_type='blender')
    - For 3D Gaussian Splatting data (62 columns):
        save_list_to_ply(diff_list, 'output.ply', cloud_type='3DGS')

    Inner workings:
    1. Converts the list of numpy arrays into a single stacked 2D numpy array.
    2. Determines the column names based on the cloud_type and the number of columns.
       - 'blender' (8 cols): x, y, z, nx, ny, nz, s, t
       - 'blender' (5 cols): x, y, z, s, t
       - '3DGS' (62 cols): x, y, z, nx, ny, nz, f_dc_0-2, f_rest_0-44, opacity, scale_0-2, rot_0-3
    3. Creates a structured numpy array (recarray) with appropriate data types (float32).
    4. Wraps the structured array in a PlyElement and subsequently a PlyData object.
    5. Writes the PlyData object to the specified path.

    :param data_list: List of numpy array objects (each array is a point's data).
    :type data_list: list of np.ndarray
    :param path: Destination file path for the .ply file.
    :type path: str
    :param cloud_type: Format type ('blender' or '3DGS'). Defaults to 'blender'.
    :type cloud_type: str
    """
    if not data_list:
        print("Empty data list provided. Nothing to save.")
        return

    # Convert list of arrays to a single 2D numpy array
    data = np.array(data_list)
    num_points, num_cols = data.shape

    # Define property names based on type and column count
    if cloud_type == 'blender':
        if num_cols == 8:
            properties = ['x', 'y', 'z', 'nx', 'ny', 'nz', 's', 't']
        elif num_cols == 5:
            properties = ['x', 'y', 'z', 's', 't']
        else:
            properties = [f'v{i}' for i in range(num_cols)]
    elif cloud_type == '3DGS':
        if num_cols == 62:
            properties = [
                'x', 'y', 'z', 'nx', 'ny', 'nz',
                'f_dc_0', 'f_dc_1', 'f_dc_2'
            ]
            properties += [f'f_rest_{i}' for i in range(45)]
            properties += ['opacity', 'scale_0', 'scale_1', 'scale_2', 'rot_0', 'rot_1', 'rot_2', 'rot_3']
        else:
            properties = [f'v{i}' for i in range(num_cols)]
    else:
        # Fallback to generic names if type is unknown
        properties = [f'v{i}' for i in range(num_cols)]

    # Create structured array for plyfile
    # Using 'f4' (float32) for all properties as seen in common PLY files
    dtype = [(p, 'f4') for p in properties]
    structured_array = np.empty(num_points, dtype=dtype)

    for i, p in enumerate(properties):
        structured_array[p] = data[:, i]

    # Create PlyElement and PlyData
    el = PlyElement.describe(structured_array, 'vertex')
    ply_data = PlyData([el])

    # construct save name
    x = datetime.now()
    time = x.strftime("%j_%H:%M")

    save_path = os.path.join(path, "difference-" + time)

    # Save to file
    ply_data.write(save_path)
    print(f"Successfully saved {num_points} points to {path}")

    return save_path

def load_ply_data(path, cloud_type = "3DGS"):
    '''  
    :param path: path to cloud point
    :param cloud_type: Possible values "3DGS" and "blender"
    '''
    
    match cloud_type:
        case "3DGS":
            return load_ply_3DGS(path)
        case "blender":
            return load_ply_blender(path)
    
    return None


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
                        np.asarray(plydata.elements[0]['t'],)
                        ), axis=1)
        
    else:
        data = np.stack((np.asarray(plydata.elements[0]['x']),
                        np.asarray(plydata.elements[0]['y']),
                        np.asarray(plydata.elements[0]['z']),
                        np.asarray(plydata.elements[0]['s']),
                        np.asarray(plydata.elements[0]['t'],)
                        ), axis=1)

    return data


def load_ply_aligned(path: str):
    '''
    Deprecated
    '''
    plydata = get_plydata(path)

    data = np.stack((np.asarray(plydata.elements[0]["x"]),
                    np.asarray(plydata.elements[0]["y"]),
                    np.asarray(plydata.elements[0]["z"]),
                    np.asarray(plydata.elements[0]["nx"]),
                    np.asarray(plydata.elements[0]["ny"]),
                    np.asarray(plydata.elements[0]["nz"])
                    ), axis=1)

    return data 