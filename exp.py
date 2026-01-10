'''
File for experimentation and figuring out what is what.
'''
import os
from config import PATH_TO_MODEL_1, PATH_TO_MODEL_2, MODEL_ITER
from diff import get_plydata, load_ply, prep_path, save_np_to_csv

# pcd = point cloud data
pcd = load_ply(prep_path(PATH_TO_MODEL_2))

columns = get_plydata(prep_path(PATH_TO_MODEL_2)).elements[0].properties
save_np_to_csv(pcd, "test2", columns, path="output")
