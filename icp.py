import open3d as o3d
import numpy as np
import copy

def perform_icp(source, target, threshold=0.02, trans_init=np.identity(4)):
    """
    Perform point-to-plane ICP registration using Open3D.
    
    Args:
        source (o3d.geometry.PointCloud): The source point cloud to be aligned.
        target (o3d.geometry.PointCloud): The target point cloud to align to.
        threshold (float): Distance threshold for matching.
        trans_init (np.ndarray): Initial 4x4 transformation matrix.
        
    Returns:
        o3d.pipelines.registration.RegistrationResult: The registration result.
    """
    # Estimate normals if not present (required for point-to-plane)
    if not source.has_normals():
        source.estimate_normals(
            search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
            
    if not target.has_normals():
        target.estimate_normals(
            search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
            
    # Point-to-plane ICP
    reg_p2l = o3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPlane())
        
    return reg_p2l
