import maya.cmds as cmds
import os

def export_geo_as_fbx():
    # Get the name of the currently opened Maya file
    current_file = cmds.file(query=True, sceneName=True)
    if not current_file:
        cmds.warning("No file is currently opened.")
        return

    # Get the name of the Geo group
    geo_group_name = 'Geo'
    if not cmds.objExists(geo_group_name):
        cmds.warning("The 'Geo' group does not exist in the scene.")
        return

    # Create an export folder in the same directory as the Maya file
    export_folder = os.path.dirname(current_file)
    export_file = os.path.join(export_folder, os.path.splitext(os.path.basename(current_file))[0] + '.fbx')

    # Select all objects in the Geo group
    cmds.select(clear=True)
    cmds.select(geo_group_name, hierarchy=True)

    # Export the selection as an FBX file
    try:
        cmds.file(export_file, force=True, options="v=0;", type="FBX export", pr=True, es=True)
        print("FBX export successful:", export_file)
    except Exception as e:
        cmds.warning("FBX export failed: {}".format(str(e)))

# Call the export_geo_as_fbx function
export_geo_as_fbx()