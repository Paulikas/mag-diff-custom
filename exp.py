'''
File for experimentation and figuring out what is what.
'''

import os

import open3d as o3d

from utils.ply_files_handler import save_list_to_ply
from config import ERROR_MARGIN, PATH_TO_MODEL_1, PATH_TO_MODEL_2, MODEL_ITER
from config import PATH_TO_BLENDER, BLENDER_MODELS
from diff import get_diff, get_plydata, load_ply_blender, prep_path_3DGS, save_np_to_csv
from icp import perform_icp, save_icp_transform

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

# Aligning point clouds using ICP



# 0. prepare paths to models
path1 = os.path.join(PATH_TO_MODEL_1, "iteration_" + MODEL_ITER[0], 'scene_point_cloud.ply')
path2 = os.path.join(PATH_TO_MODEL_2, "iteration_" + MODEL_ITER[0], 'scene_point_cloud.ply')

source = perform_icp(path1, path2)

save_path = save_icp_transform(source)

# Getting data to right format
print("Transformed point cloud data")

pld = get_plydata(save_path)

print(pld)
print(len(pld.elements[0].data['x']))

print("Original point cloud data")

pld2 = get_plydata(path1)

print(pld2)
print(len(pld2.elements[0].data['x']))

print("Target point cloud data")

pld3 = get_plydata(path2)

print(pld3)
print(len(pld3.elements[0].data['x']))

# ----------------------------------

