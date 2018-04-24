# Import PCL module
import pcl

# Load Point Cloud file
cloud = pcl.load_XYZRGB('tabletop.pcd')


# 1-Voxel Grid filter (AVERAGES by CUBES!!!!!)
vox = cloud.make_voxel_grid_filter()
LEAF_SIZE = 0.01
vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)
cloud_filtered = vox.filter()
filename = 'tabletop_vgf_ptf.pcd'
pcl.save(cloud_filtered, filename)


## 2-PassThrough filter (SLICES GEOMETRY by PLANES!!!!)
passthrough = cloud_filtered.make_passthrough_filter()
filter_axis = 'z'
passthrough.set_filter_field_name(filter_axis)
passthrough.set_filter_limits(0.6, 1.1)
cloud_filtered = passthrough.filter()
filename = 'tabletop_vgf_ptf.pcd'
pcl.save(cloud_filtered, filename)


# 3-RANSAC plane segmentation
seg = cloud_filtered.make_segmenter()
# Set the model you wish to fit 
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_method_type(pcl.SAC_RANSAC)
# Max distance for a point to be considered fitting the model
# Experiment with different values for max_distance for segmenting the table
max_distance = 0.01
seg.set_distance_threshold(max_distance)
# Call the segment function to obtain set of inlier indices and model coeffs
inliers, coefficients = seg.segment() # list, list
# Extract inliers
extracted_inliers = cloud_filtered.extract(inliers, negative=False)
filename = 'tabletop_vgf_ptf_extracted_inliers.pcd'
pcl.save(extracted_inliers, filename)
# Extract outliers
extracted_outliers = cloud_filtered.extract(inliers, negative=True)
filename = 'tabletop_vgf_ptf_extracted_outliers.pcd'
pcl.save(extracted_outliers, filename)

# 4- statistical filter
outlier_filter = cloud_filtered.make_statistical_outlier_filter()
# number of neighbor points to analyze for any given point
outlier_filter.set_mean_k(50)
# threshold scale value
x = 1.0
# outlier = a point with a mean dist > global (mean dist + x * stddev)
outlier_filter.set_std_dev_mul_thresh(x)
# call filter function
cloud_filtered = outlier_filter.filter()
filename = 'tabletop_vgf_ptf_outlierfilter.pcd'
pcl.save(cloud_filtered, filename)