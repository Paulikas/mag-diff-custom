'''
File for experimentation and figuring out what is what.
'''
from utils.ply_files_handler import save_list_to_ply
import os
from config import ERROR_MARGIN, PATH_TO_MODEL_1, PATH_TO_MODEL_2, MODEL_ITER
from config import PATH_TO_BLENDER, BLENDER_MODELS
from diff import get_diff, get_plydata, load_ply_blender, prep_path_3DGS, save_np_to_csv

# pcd = point cloud data
# pcd = load_ply_3DGS(prep_path_3DGS(PATH_TO_MODEL_2))

# columns = get_plydata(prep_path_3DGS(PATH_TO_MODEL_2)).elements[0].properties
# save_np_to_csv(pcd, "test2", columns, path="output")

# ----------------------------
# for i in BLENDER_MODELS:

#     print(i)

#     path = os.path.join(PATH_TO_BLENDER, BLENDER_MODELS[i])

#     pld = get_plydata(path)
#     pcd = load_ply_blender(path)

#     columns = pld.elements[0].properties

#     print(pld)

#     print(pcd)

#     save_np_to_csv(pcd, i, columns, path="output\\blender")

# ----------------------------------

# path1 = os.path.join(PATH_TO_BLENDER, BLENDER_MODELS['cube'])
# path2 = os.path.join(PATH_TO_BLENDER, BLENDER_MODELS['cube_with_addon'])


# pcd1 = load_ply_blender(path1)
# pcd2 = load_ply_blender(path2)

# diff =  get_diff(pcd1, pcd2)
# save_list_to_ply(diff, "output\diff\difference1.ply", cloud_type='blender')

# diff_after = load_ply_blender("output\diff\difference1.ply")

# ply_diff = get_plydata("output\diff\difference1.ply")
# ply2 = get_plydata(path2)

# print(ply2)
# print(pcd2)

# print(ply_diff)
# print(diff_after)


# ----------------------------------

import open3d as o3d
from icp import perform_icp
import numpy as np

# 0. prepare paths to models
path1 = os.path.join(PATH_TO_MODEL_1, "iteration_" + MODEL_ITER[0], 'scene_point_cloud.ply')
path2 = os.path.join(PATH_TO_MODEL_2, "iteration_" + MODEL_ITER[0], 'scene_point_cloud.ply')

# 1. Load your point clouds from the data/stalas folder
source = o3d.io.read_point_cloud(path1)
target = o3d.io.read_point_cloud(path2)

# 2. (Optional) Define a distance threshold and initial transformation
threshold = ERROR_MARGIN 
trans_init = np.identity(4)

# 3. Perform ICP alignment
# This function handles normal estimation automatically if needed
reg_result = perform_icp(source, target, threshold, trans_init)

# 4. Apply the resulting transformation to the source cloud
source.transform(reg_result.transformation)

# 5. Check the fitness and inlier RMSE
print(f"Fitness: {reg_result.fitness}")
print(f"Inlier RMSE: {reg_result.inlier_rmse}")

# 6. Save the aligned point cloud
o3d.io.write_point_cloud("output/stalas/aligned_pointcloud.ply", source)