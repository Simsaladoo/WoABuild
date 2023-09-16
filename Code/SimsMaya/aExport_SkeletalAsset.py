print("Running Skeletal Mesh Export")

import maya.cmds as cmds
import os

# Get the name and directory of the current file
file_path = cmds.file(q=True, sn=True)
file_dir = os.path.dirname(file_path)
file_name = os.path.splitext(os.path.basename(file_path))[0]

# Select everything in the scene
cmds.select(all=True)

# Export as FBX
export_path = os.path.join(file_dir, file_name + ".fbx")
cmds.file(export_path, force=True, options="v=0;", type="FBX export", pr=True, es=True)

print("FBX exported to: " + export_path)