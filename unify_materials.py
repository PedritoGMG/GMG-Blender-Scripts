import bpy

def unify_materials():
    # Define unified material name
    unified_material_name = "UnifiedMaterial"
    
    # Check if unified material already exists
    unified_material = bpy.data.materials.get(unified_material_name)
    
    if unified_material is None:
        # Create material if it doesn't exist
        unified_material = bpy.data.materials.new(name=unified_material_name)
        unified_material.use_nodes = True  # Use nodes for texture handling
    
    # Find and get texture from first material in scene
    texture = None
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            for material_slot in obj.material_slots:
                if material_slot.material is not None:
                    # Check if material has texture
                    for node in material_slot.material.node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.image is not None:
                            texture = node.image
                            break
            if texture:
                break

    if texture:
        # Assign texture to unified material
        if unified_material.use_nodes:
            bsdf = unified_material.node_tree.nodes.get('Principled BSDF')
            texture_node = unified_material.node_tree.nodes.new(type='ShaderNodeTexImage')
            texture_node.image = texture
            unified_material.node_tree.links.new(bsdf.inputs['Base Color'], texture_node.outputs['Color'])
    else:
        print("No texture found in scene materials.")
        return

    # Change all object materials to this unified material
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            for material_slot in obj.material_slots:
                material_slot.material = unified_material

    print(f" !! All materials have been unified to {unified_material_name}.")

unify_materials()