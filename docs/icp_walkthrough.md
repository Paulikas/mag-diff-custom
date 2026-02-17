# ICP Implementation Walkthrough

I have implemented the Iterative Closest Point (ICP) algorithm using the Open3D library in `icp.py`. As requested, I've used the **point-to-plane** variation.

## Changes Made

### [icp.py](../icp.py)

- Implemented `perform_icp(source, target, threshold, trans_init)`.
- Added automatic normal estimation for both source and target point clouds if they are missing (essential for point-to-plane ICP).

## How to Use the Function

To use the `perform_icp` function in your scripts, you can import it and follow these steps:

```python
import open3d as o3d
from icp import perform_icp
import numpy as np

# 1. Load your point clouds from the data/stalas folder
source = o3d.io.read_point_cloud("data/stalas/your_source_cloud.ply")
target = o3d.io.read_point_cloud("data/stalas/your_target_cloud.ply")

# 2. (Optional) Define a distance threshold and initial transformation
threshold = 0.02
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
o3d.io.write_point_cloud("output/aligned_pointcloud.ply", source)
```

### Parameters:
- `source`: The `open3d.geometry.PointCloud` that you want to move.
- `target`: The `open3d.geometry.PointCloud` that you want to align to (stays static).
- `threshold`: The maximum distance between corresponding points. Points further apart than this won't be considered matches.
- `trans_init`: A 4x4 numpy array representing the initial transformation. Defaults to the identity matrix.

### Returns:
- An `open3d.pipelines.registration.RegistrationResult` object, which contains the `transformation` matrix, `fitness`, and `inlier_rmse`.
