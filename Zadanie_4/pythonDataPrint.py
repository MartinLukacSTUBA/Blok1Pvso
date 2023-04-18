import pyntcloud
import open3d as o3d
# Toto je zbytočné podľa mna
# # Nastavenie cesty k súboru s mračnom bodov
# filename = "/home/d618/Desktop/cv3-vido-lukac/output.ply"
#
# # Načítanie mračna bodov
# cloud = pyntcloud.PyntCloud.from_file(filename)
# 
# # Zobrazenie informácií o mračne
# print(cloud)

# Načítanie súboru v .ply formáte
pcd = o3d.io.read_point_cloud("/home/d618/Desktop/cv3-vido-lukac/output.ply")

# Odstránenie outliers pomocou RANSAC algoritmu
pcd_cleaned, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

# Vytvorenie dvoch okien pre zobrazenie mračna
vis = o3d.visualization.VisualizerWithKeyCallback()
vis2 = o3d.visualization.VisualizerWithKeyCallback()

# Pridanie mračna do prvého okna
vis.create_window(window_name='Original point cloud')
vis.add_geometry(pcd)

# Pridanie mračna bez outlierov do druhého okna
vis2.create_window(window_name='Cleaned point cloud')
vis2.add_geometry(pcd_cleaned)

# aj toto je podľa mna zbytocne
# # Funkcia na získanie klávesnice udalosti pre zobrazenie oboch okien naraz
# def animation_callback(vis):
#     vis2.poll_events()
#     vis2.update_renderer()
#     return False
#
# # Spustenie vizualizácie oboch okien s možnosťou zmeny pohľadu pomocou myši
# o3d.visualization.draw_geometries_with_animation_callback([pcd, pcd_cleaned], animation_callback)



##: je to po BOD 3




# ODTIALTO UZ IDE PROGRAM 4
import numpy as np
import pyntcloud
import open3d as o3d
from sklearn.cluster import KMeans, DBSCAN

# Nastavenie cesty k súboru s mračnom bodov
filename = "/home/d618/Desktop/cv3-vido-lukac/output.ply"

# Načítanie mračna bodov
pcd = o3d.io.read_point_cloud(filename)

# Odstránenie outliers pomocou RANSAC algoritmu
pcd_cleaned, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

# K-means algoritmus pre segmentáciu priestoru do klastrov
kmeans = KMeans(n_clusters=10, random_state=0)
kmeans_labels = kmeans.fit_predict(pcd_cleaned.points)

# DBSCAN algoritmus pre segmentáciu priestoru do klastrov
dbscan_labels = np.array(pcd_cleaned.cluster_dbscan(eps=0.1, min_points=50, print_progress=True))

# Vytvorenie farieb pre zobrazenie výsledkov segmentácie
colors = np.random.rand(max(kmeans_labels.max(), dbscan_labels.max()) + 1, 3)

# Pridanie farieb pre jednotlivé body v mračne
pcd_cleaned.colors = o3d.utility.Vector3dVector(colors[kmeans_labels])
pcd_cleaned.colors = o3d.utility.Vector3dVector(colors[dbscan_labels])

# Vytvorenie dvoch okien pre zobrazenie mračna
vis = o3d.visualization.VisualizerWithKeyCallback()
vis2 = o3d.visualization.VisualizerWithKeyCallback()

# Pridanie mračna do prvého okna
vis.create_window(window_name='K-means clustering')
vis.add_geometry(pcd_cleaned)

# Pridanie mračna do druhého okna
vis2.create_window(window_name='DBSCAN clustering')
vis2.add_geometry(pcd_cleaned)

# # Funkcia na získanie klávesnice udalosti pre zobrazenie oboch okien naraz
# def animation_callback(vis):
#     vis2.poll_events()
#     vis2.update_renderer()
#     return False
#
# # Spustenie vizualizácie oboch okien s možnosťou zmeny pohľadu pomocou myši
# o3d.visualization.draw_geometries_with_animation_callback([pcd_cleaned], animation_callback)
