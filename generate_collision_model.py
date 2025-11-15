import bpy
import bmesh

def create_collision_model():
    # Get selected object
    obj = bpy.context.object
    if obj is None or obj.type != 'MESH':
        print("Please select a mesh object before running this script.")
        return
    
    # Duplicate object for collision model
    collision_obj = obj.copy()
    collision_obj.data = obj.data.copy()
    collision_obj.name = obj.name + "_collision"
    bpy.context.collection.objects.link(collision_obj)

    # Apply Convex Hull to ensure convex collision
    bpy.context.view_layer.objects.active = collision_obj
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(collision_obj.data)
    bmesh.ops.convex_hull(bm, input=bm.verts)
    bmesh.update_edit_mesh(collision_obj.data)
    bpy.ops.object.mode_set(mode='OBJECT')

    # Apply flat shading (prevents issues with Source Engine)
    bpy.ops.object.shade_flat()

    # Create red material to identify as collision model
    material = bpy.data.materials.get("CollisionMaterial")
    if material is None:
        material = bpy.data.materials.new(name="CollisionMaterial")
        material.diffuse_color = (1, 0, 0, 1)  # Red color
    
    collision_obj.data.materials.clear()
    collision_obj.data.materials.append(material)

    # Apply transformations
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    # Export as SMD (requires Blender Source Tools)
    smd_path = bpy.path.abspath("//collision_model.smd")
    bpy.ops.export_scene.smd(filepath=smd_path, export_selected=True)

    print(f" !! Collision model exported as {smd_path}")

# Execute function
create_collision_model()