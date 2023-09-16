

import maya.cmds as cmds

# Define the path to the FBX file you want to import
fbx_file_path = r"D:/UE4/Tailwind_R E B U I L D/Equipment/Weapons/_wWeapon_REF___TEMPLATE.fbx"

# Import the FBX file into the current scene
cmds.file(fbx_file_path, i=True)