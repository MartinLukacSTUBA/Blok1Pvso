import open3d as o3d
from freenect2 import Device, FrameType

# Open the default device and capture a color and depth frame.
device = Device()
frames = {}
with device.running():
    for type_, frame in device:
        frames[type_] = frame
        if FrameType.Color in frames and FrameType.Depth in frames:
            break

# Use the factory calibration to undistort the depth frame and register the RGB
# frame onto it.
rgb, depth = frames[FrameType.Color], frames[FrameType.Depth]
undistorted, registered, big_depth = device.registration.apply(
    rgb, depth, with_big_depth=True)

# Combine the depth and RGB data together into a single point cloud.
with open('output.pcd', 'wb') as fobj:
    device.registration.write_pcd(fobj, undistorted, registered)

with open('output_big.pcd', 'wb') as fobj:
    device.registration.write_big_pcd(fobj, big_depth, rgb)

# nacitanie s pcd
pcd = o3d.io.read_point_cloud("output.pcd")

# ulozenie ply formatu
o3d.io.write_point_cloud("./output.ply", pcd)


pcd_big = o3d.io.read_point_cloud("output_big.pcd")


o3d.io.write_point_cloud("./output_big.ply", pcd_big)


