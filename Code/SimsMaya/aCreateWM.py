import maya.cmds as cmds


# Find all weapon geometry under the "Geo" group
geo_group = cmds.ls('Geo', g=True)
selectgeo = cmds.select('wSheathe_*')


print(selectgeo)

def ShiftWM():
    for shape in cmds.ls(type='mesh'):
        # Center the pivot point
        cmds.xform(new_transform, cp=True)

        # Re-orient rotation to point towards world X
        cmds.makeIdentity(new_transform, apply=True, t=0, r=1, s=0, n=0)
        cmds.rotate(90, 0, 0, new_transform, r=True, os=True)

        # Move the shape to the world origin
        cmds.move(0, 0, 0, new_transform, absolute=True, worldSpace=True)
        


def CreateCopies():
    for shape in cmds.ls(type='mesh'):
        # Get the transform node for the shape
        transform = cmds.listRelatives(shape, parent=True, fullPath=True)[0]

        new_transform = cmds.duplicate(transform, rr=True)[0]
        new_shape = cmds.listRelatives(new_transform, shapes=True, fullPath=True)[0]
        





        
        
        
        
CreateCopies()
# ShiftWM()