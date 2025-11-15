import bpy
import math

# Configure object and camera names
target_object = bpy.data.objects['prop_static_2']
camera = bpy.data.objects['Camera']
output_path = '//renders/x_axis/'  # Output path (relative to .blend file)

# Number of angles (8 renders at 45 degree intervals)
num_angles = 8

# Camera configuration
distance = 15  # Distance from camera to object

for i in range(num_angles):
    # Calculate rotation angle (45 degrees each step)
    angle = (2 * math.pi / num_angles) * i
    
    # Calculate new camera position around the object (X-axis rotation)
    camera.location.x = target_object.location.x  # Maintain X position
    camera.location.y = target_object.location.y + distance * math.cos(angle)  # Y movement
    camera.location.z = target_object.location.z + distance * math.sin(angle)  # Z movement (altitude)

    # Point camera towards the object
    camera.rotation_euler[0] = angle - math.pi / 2  # X-axis rotation to face object
    camera.rotation_euler[1] = 0  # No Y rotation
    camera.rotation_euler[2] = 0  # No Z rotation

    # Render and save image with transparency
    bpy.context.scene.render.filepath = f"{output_path}render_x_{i * 45}.png"
    bpy.ops.render.render(write_still=True)