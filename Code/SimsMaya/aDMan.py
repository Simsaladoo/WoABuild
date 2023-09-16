# D:/UE4/Tailwind_R E B U I L D/Characters/DebugStatic.fbx

import maya.cmds as cmds

# Define the path to the FBX file you want to import
fbx_file_path = r"D:/UE4/Tailwind_R E B U I L D/Characters/DebugStatic.fbx"

# Import the FBX file into the current scene
cmds.file(fbx_file_path, i=True)