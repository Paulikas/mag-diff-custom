from datetime import datetime
import open3d as o3d
import numpy as np
import copy
import os
from plyfile import PlyData

from utils.logger import get_logger
logger = get_logger(__name__)

def perform_icp(path1, path2, threshold=0.02, trans_init=np.identity(4)):
    """
    Perform point-to-plane ICP registration using Open3D.

    Path 1 is source, path 2 is target. Transformed source point cloud is returned.
    """

    # 1. Load your point clouds from the data/stalas folder
    source = o3d.io.read_point_cloud(path1)
    target = o3d.io.read_point_cloud(path2)

    print(len(source.points))
    print(source)
    print(len(target.points))

    # 2. Perform ICP alignment
    reg_result = o3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint()
    )

    # 3. Apply the resulting transformation to the source cloud keeping all attributes
    plydata = PlyData.read(path1)
    
    x = plydata.elements[0].data['x']
    y = plydata.elements[0].data['y']
    z = plydata.elements[0].data['z']
    
    pts = np.vstack((x, y, z, np.ones(x.shape[0])))
    pts_trans = (reg_result.transformation @ pts)
    
    plydata.elements[0].data['x'] = pts_trans[0]
    plydata.elements[0].data['y'] = pts_trans[1]
    plydata.elements[0].data['z'] = pts_trans[2]
    
    # Check for normals and rotate them if they exist
    names = plydata.elements[0].data.dtype.names
    if names is not None and 'nx' in names and 'ny' in names and 'nz' in names:
        nx = plydata.elements[0].data['nx']
        ny = plydata.elements[0].data['ny']
        nz = plydata.elements[0].data['nz']
        normals = np.vstack((nx, ny, nz))
        rot = reg_result.transformation[:3, :3]
        normals_trans = (rot @ normals)
        plydata.elements[0].data['nx'] = normals_trans[0]
        plydata.elements[0].data['ny'] = normals_trans[1]
        plydata.elements[0].data['nz'] = normals_trans[2]

    # 4. Check the fitness and inlier RMSE
    print("Alignment complete")
    print(f"Fitness: {reg_result.fitness}")
    print(f"Inlier RMSE: {reg_result.inlier_rmse}")
    
    logger.info(f"Fitness: {reg_result.fitness}")
    logger.info(f"Inlier RMSE: {reg_result.inlier_rmse}")

    return plydata

def save_icp_transform(source) -> str:
    '''
    Returns path to saved file.
    '''
    x = datetime.now()
    time = x.strftime("%j_%H:%M")

    save_path = "output/stalas/aligned_pointcloud " + time + ".ply"
    
    # Check if the source is PlyData or Open3D point cloud
    if isinstance(source, o3d.geometry.PointCloud):
        o3d.io.write_point_cloud(os.path.join(save_path), source)
    else:
        # Assuming it's a PlyData object
        source.write(os.path.join(save_path))

    print("Transformed point cloud data saved to " + save_path)
    logger.info("Transformed point cloud data saved to " + save_path)

    return save_path