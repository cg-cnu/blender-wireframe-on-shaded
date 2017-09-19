# Wireframe on shaded
# Toggle the display of wireframe on the objects visible in the viewport

bl_info = {
    "name": "Wireframe on shaded",
    "description": "Toggle wireframe on shaded for all objects in the viewport with Shift + W",
    "author": "Sreenivas Alapati",
    "version": (1, 0),
    "blender": (2, 9, 0),
    "category": "3D View"}

import bpy

def main(context):            
    meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    wireframeMeshes = [mesh for mesh in meshes if mesh.show_wire == True]
    
    if wireframeMeshes:
        for mesh in wireframeMeshes:
            mesh.show_wire = mesh.show_all_edges = False
    else:
        for mesh in meshes:
            mesh.show_wire = mesh.show_all_edges = True
    
class wireframeOnShaded(bpy.types.Operator):
    """ Displays wire frame on shaded by enabling showing wire and show all edges on all objects in the viewport
    """
    bl_idname = "object.wireframe_on_shaded"
    bl_label = "Wireframe on shaded"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(wireframeOnShaded)
    km = bpy.context.window_manager.keyconfigs.default.keymaps['Object Mode']
    kmi = km.keymap_items.new("object.wireframe_on_shaded", 'W', 'PRESS', shift=True)
   
def unregister():
    bpy.utils.unregister_class(wireframeOnShaded)
    km = bpy.context.window_manager.keyconfigs.default.keymaps['Object Mode']
    for kmi in (kmi for kmi in km.keymap_items if kmi.idname in {"object.wireframe_on_shaded", }):
        km.keymap_items.remove(kmi) 

if __name__ == "__main__":
    register()