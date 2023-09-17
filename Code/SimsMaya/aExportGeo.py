import maya.cmds as cmds
import os
from MayaPaths import get_art_source_dir

    
    
def export_cmd(export_file):
    # Export the selection as an FBX file
    try:
        cmds.file(export_file, force=True, options="v=0;", type="FBX export", pr=True, es=True)
        print("FBX export successful:", export_file)
    except Exception as e:
        cmds.warning("FBX export failed: {}".format(str(e)))
   
def choose_export_path(is_relative_path, current_file):
    if is_relative_path:
        # Create an export folder in the same directory as the Maya file
        export_folder = os.path.dirname(current_file)
        export_file = os.path.join(export_folder, os.path.splitext(os.path.basename(current_file))[0] + '.fbx')
        return export_file
    else:
        publish_path = get_art_source_dir() + '/Worldmap/WorldmapActor/Worldchunks/'
        export_file = os.path.join(publish_path, os.path.splitext(os.path.basename(current_file))[0] + '.fbx')
        return export_file
        
def geo_export_selection(current_file, is_relative):
    # Get the name of the Geo group
    geo_group_name = 'Geo'
    if not cmds.objExists(geo_group_name):
        cmds.warning("The 'Geo' group does not exist in the scene.")
        return

    export_file = choose_export_path(is_relative, current_file)
    # Select all objects in the Geo group
    cmds.select(clear=True)
    cmds.select(geo_group_name, hierarchy=True)
    
    # Export the selection as an FBX file
    export_cmd(export_file)

        
def export_geo_as_fbx(is_relative):
    # Get the name of the currently opened Maya file
    current_file = cmds.file(query=True, sceneName=True)
    if not current_file:
        cmds.warning("No file is currently opened.")
        return 
    ## create selection to export
    geo_export_selection(current_file, is_relative)


def export_worldmap_geo():
    export_geo_as_fbx(True)
    export_geo_as_fbx(False)