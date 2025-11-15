import bpy

# Fix UV layer names to prevent texture issues when merging models
# This solves the problem of incorrect texture assignment when combining multiple objects

for obj in bpy.context.selected_objects:
    try:
        # Rename stencil UV layer to standard name
        obj.data.uv_layers.data.uv_layer_stencil.name = 'UVmap'
    except:
        continue  # Skip objects without the stencil layer