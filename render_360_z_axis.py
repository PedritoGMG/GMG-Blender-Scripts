import bpy
import math

# Configure object and camera names
target_object = bpy.data.objects['prop_static_2']
camera = bpy.data.objects['Camera']
output_path = '//renders/z_axis/'  # Output path (relative to .blend file)

# Number of angles (8 renders at 45 degree intervals)
num_angles = 8

# Camera configuration
distance = 15  # Distance from camera to object
height = 0     # Camera height relative to object

for i in range(num_angles):
    # Calculate rotation angle (45 degrees each step)
    angle = (2 * math.pi / num_angles) * i
    
    # Calculate new camera position around the object (Z-axis rotation)
    camera.location.x = target_object.location.x + distance * math.cos(angle)
    camera.location.y = target_object.location.y + distance * math.sin(angle)
    camera.location.z = target_object.location.z + height  # Maintain Z height

    # Point camera towards the object with 90-degree correction
    camera.rotation_euler[2] = angle + math.pi / 2  # Z-axis rotation to face object

    # Render and save image with transparency
    bpy.context.scene.render.filepath = f"{output_path}render_z_{i * 45}.png"
    bpy.ops.render.render(write_still=True)