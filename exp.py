'''
File for experimentation and figuring out what is what.
'''
import os
from config import PATH_TO_MODEL_1, PATH_TO_MODEL_2, MODEL_ITER
from config import PATH_TO_BLENDER, BLENDER_MODELS
from diff import get_plydata, load_ply_blender, prep_path_3DGS, save_np_to_csv

# pcd = point cloud data
# pcd = load_ply_3DGS(prep_path_3DGS(PATH_TO_MODEL_2))

# columns = get_plydata(prep_path_3DGS(PATH_TO_MODEL_2)).elements[0].properties
# save_np_to_csv(pcd, "test2", columns, path="output")

for i in BLENDER_MODELS:

    print(i)

    path = os.path.join(PATH_TO_BLENDER, BLENDER_MODELS[i])

    pld = get_plydata(path)
    pcd = load_ply_blender(path)

    columns = pld.elements[0].properties

    print(pld)

    print(pcd)

    save_np_to_csv(pcd, i, columns, path="output\\blender")
