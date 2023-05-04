import pyntcloud
import open3d as o3d

pcd = o3d.io.read_point_cloud("/home/d618/Desktop/cv3-vido-lukac/output.ply")

# RNSAC
pcd_cleaned, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)


vis = o3d.visualization.VisualizerWithKeyCallback()
vis2 = o3d.visualization.VisualizerWithKeyCallback()


vis.create_window(window_name='Original point cloud')
vis.add_geometry(pcd)

vis2.create_window(window_name='Cleaned point cloud')
vis2.add_geometry(pcd_cleaned)

def animation_callback(vis):
    vis2.poll_events()
    vis2.update_renderer()
    return False

o3d.visualization.draw_geometries_with_animation_callback([pcd, pcd_cleaned], animation_callback)



##: je to po BOD 3




# ODTIALTO UZ IDE PROGRAM 4
import numpy as np
import pyntcloud
import open3d as o3d
from sklearn.cluster import KMeans, DBSCAN

filename = "/home/d618/Desktop/cv3-vido-lukac/output.ply"

pcd = o3d.io.read_point_cloud(filename)

# RNSAC
pcd_cleaned, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

# K-means
kmeans = KMeans(n_clusters=10, random_state=0)
kmeans_labels = kmeans.fit_predict(pcd_cleaned.points)

# DBSCAN
dbscan_labels = np.array(pcd_cleaned.cluster_dbscan(eps=0.1, min_points=50, print_progress=True))


colors = np.random.rand(max(kmeans_labels.max(), dbscan_labels.max()) + 1, 3)


pcd_cleaned.colors = o3d.utility.Vector3dVector(colors[kmeans_labels])
pcd_cleaned.colors = o3d.utility.Vector3dVector(colors[dbscan_labels])


vis = o3d.visualization.VisualizerWithKeyCallback()
vis2 = o3d.visualization.VisualizerWithKeyCallback()


vis.create_window(window_name='K-means clustering')
vis.add_geometry(pcd_cleaned)


vis2.create_window(window_name='DBSCAN clustering')
vis2.add_geometry(pcd_cleaned)


def animation_callback(vis):
    vis2.poll_events()
    vis2.update_renderer()
    return False


o3d.visualization.draw_geometries_with_animation_callback([pcd_cleaned], animation_callback)
