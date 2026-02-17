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

    # Save to file
    ply_data.write(path)
    print(f"Successfully saved {num_points} points to {path}")
