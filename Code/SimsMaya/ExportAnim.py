import maya.cmds as cmds


cmds.select (clear=True)
cmds.select ('aMasterSkel_M:*')
cmds.select ("Handles", add=True, hierarchy=True)

# Get the name of the current scene
scene_name = cmds.file(query=True, shortName=True, withoutExtension=True)

# Set the range of frames to bake
start_frame = cmds.playbackOptions(query=True, min=True)
end_frame = cmds.playbackOptions(query=True, max=True)

# Get a list of all joints in the scene
joints = cmds.ls(type="joint")

# Set the keyframe option to "insert" to bake animation onto the joints
cmds.bakeResults(joints, t=(start_frame, end_frame), sb=1, pok=True, at=["tx","ty","tz","rx","ry","rz"])

# Export the scene as an FBX with the same name as the scene
export_path = scene_name + ".fbx"
cmds.file(export_path, force=True, options="v=0", type="FBX export", exportSelected=False)