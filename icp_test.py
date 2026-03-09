import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
import copy

# Read source and target PCD
demo_pcds = o3d.data.DemoICPPointClouds()
source = o3d.io.read_point_cloud(demo_pcds.paths[0]) # PointCloud with 191397 points.
#source.dimension( )  -> 3
target = o3d.io.read_point_cloud(demo_pcds.paths[1]) # PointCloud with 137833 points.
#target.dimension( )  -> 3

o3d.visualization.draw_plotly([source],
                                  zoom=0.455,
                                  front=[-0.4999, -0.1659, -0.8499],
                                  lookat=[2.1813, 2.0619, 2.0999],
                                  up=[0.1204, -0.9852, 0.1215])
 
o3d.visualization.draw_plotly([target],
                                  zoom=0.455,
                                  front=[-0.4999, -0.1659, -0.8499],
                                  lookat=[2.1813, 2.0619, 2.0999],
                                  up=[0.1204, -0.9852, 0.1215])


def draw_registration_result(source, target, transformation):
      source_temp = copy.deepcopy(source)
      target_temp = copy.deepcopy(target)
      source_temp.paint_uniform_color([1, 0.0706, 0])
      target_temp.paint_uniform_color([0, 0.651, 0.929])
      source_temp.transform(transformation)
      o3d.visualization.draw_plotly([source_temp, target_temp])
 
 
# *** Initial Transformation ***
trans_init = np.asarray([[0.862, 0.011, -0.507, 0.5],
                         [-0.139, 0.967, -0.215, 0.7],
                         [0.487, 0.255, 0.835, -1.4], [0.0, 0.0, 0.0, 1.0]])
 
draw_registration_result(source, target, trans_init)

threshold = 0.02
print("Initial Alignment")
evaluation = o3d.pipelines.registration.evaluate_registration(
                       source, target, threshold, trans_init)
print(evaluation)
 
"""Initial alignment
RegistrationResult with fitness=2.740900e-02, inlier_rmse=1.259521e-02, and correspondence_set size of 5246
Access transformation to get result."""

# ******* Point-to-Point *********
threshold = 0.02
print("Apply point-to-point ICP")
reg_p2p = o3d.pipelines.registration.registration_icp(
                   source, target, threshold, trans_init,
                   o3d.pipelines.registration.TransformationEstimationPointToPoint())
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
draw_registration_result(source, target, reg_p2p.transformation)
o3d.visualization.draw_plotly(reg_p2p)
 
"""
Apply point-to-point ICP
RegistrationResult with fitness=3.132755e-02, inlier_rmse=1.168464e-02, and correspondence_set size of 5996
Access transformation to get result.
Transformation is:
[[ 0.86481662  0.0378514  -0.50084398  0.42597758]
 [-0.15157681  0.97072361 -0.18799414  0.66535821]
 [ 0.47817432  0.23769297  0.84517011 -1.35537445]
 [ 0.          0.          0.          1.        ]]
"""

threshold=0.02
print("Apply point-to-point ICP")
reg_p2p = o3d.pipelines.registration.registration_icp(
    source, target, threshold, trans_init,
    o3d.pipelines.registration.TransformationEstimationPointToPoint())
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
draw_registration_result(source, target, reg_p2p.transformation)
o3d.visualization.draw_plotly(reg_p2p)