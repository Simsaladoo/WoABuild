import maya.cmds as cmds
import os
import re

folder_path = 'D:/UE4/Tailwind_R E B U I L D/H/World48/Landscapes'
file_list = os.listdir(folder_path)
fbx_files = [file for file in file_list if file.lower().endswith('.fbx')]
total_limit = 7


# return world-aligned vector of this tile's coordinate (no Z)
def get_translation(in_x, in_y):
    ''''''
    grid_size = 201600
    out_x = in_x * grid_size
    out_y = in_y * grid_size
    
    offset_translation = (out_x, out_y, 0)
    return offset_translation

# positioner
def import_world_cell(path, reference_name, x, y):
    ''''''
    # Import the file, and then add offset to each set of objects
    cmds.file(path, reference=True, namespace=reference_name) 
    objects = cmds.namespaceInfo(reference_name, listNamespace=True)
    
    for obj in objects:
        if cmds.objExists(obj):
            landscape_coords = get_translation(x, y) 
            print("Setting Transforms on: " + (obj) + ', Coords: ' + str(landscape_coords))   
            cmds.xform(obj, translation=landscape_coords, relative=True)
    
def get_x_from_name(fbx_file):
    ''''''
    # get the x/y coords as ints from this map's name
    match = re.match(r'.*_x(\d+)_y(\d+)\.fbx', fbx_file)
    if match:
        x_value = int(match.group(1)) 
    return x_value

def get_y_from_name(fbx_file):
    ''''''
    # get the x/y coords as ints from this map's name
    match = re.match(r'.*_x(\d+)_y(\d+)\.fbx', fbx_file)
    if match:
        y_value = int(match.group(2))    
    return y_value


def import_world(reference_name, fbx_file, full_path, x_value, y_value):
    ''''''
    # if ANY landscape fbx file is not referenced currently:
    if not cmds.namespace(exists=reference_name):            
        # if x and y coords are in range of what we want to import, ref it in!
        print("Referencing " + fbx_file)    
        import_world_cell(full_path, reference_name, x_value, y_value)
        
        
def create_geo_group():
    # Select all polygon objects in the scene
    polyObjects = cmds.ls(type="mesh")
    
    # Create a new group named "Geo" if it doesn't exist
    if not cmds.objExists("Geo"):
        cmds.group(em=True, name="Geo")

    # Add selected polygon objects to the "Geo" group
    for polyObject in polyObjects:
        cmds.parent(polyObject, "Geo")

    # Deselect all objects
    cmds.select(clear=True)
    
    
def import_refs():
    # List all reference nodes in the scene
    referenceNodes = cmds.ls(type="reference")

    # Import all references
    for referenceNode in referenceNodes:
        cmds.file(referenceNode, importReference=True)

    print("All references have been imported.")
     


# references in specific sublevel    
def run_import_world_loop(x_value, y_value):
    x_range = x_value+total_limit
    y_range = y_value+total_limit
 
    # find and match the x/y ints to the filename strings
    for fbx_file in fbx_files:
        full_path = os.path.join(folder_path, fbx_file)
        reference_name = fbx_file.replace('.fbx', '')
        x_low = get_x_from_name(fbx_file)
        y_low = get_y_from_name(fbx_file)
        # print('Reading: ' + str(x_low) + ', ' + str(y_low) + '... ')

        if x_low >= x_value and x_low <= x_range:
            if y_low >= y_value and y_low <= y_range:
                print('Importing: ' + str(x_low) + ', ' + str(y_low) + '... ') 
                import_world(reference_name, fbx_file, full_path, x_low, y_low)
                
    # group them all
    create_geo_group()
    
    # Import the references when done
    import_refs()


