# Import the Maya commands library
import maya.cmds as cmds
from SimsMaya import aDMan, aCreateWorld48, aExportGeo, aOrientToEpic, aReduceWorld48


# Create a window using the cmds.window command
# give it a title, icon and dimensions
window = cmds.window( title="Sim's Tools - DEditor Library", iconName='DEditor', widthHeight=(320, 650) )

# As we add contents to the window, align them vertically
cmds.columnLayout( adjustableColumn=True )



# -------------------------------------------- Rigging ---------------------------------------------- #
# Top text header
cmds.text( label=' ', align='center' )
cmds.text( label='Rigging', align='center', fn="smallObliqueLabelFont" )
cmds.text( label=' ', align='center' )

# Take aHair and aScalp and rig them to Almerra Skeleton
cmds.button( label='Rig Hair and Scalps', command=('ButtonSkinScalp()'))

# Take wWeapon and wSheathe and rig them to Almerra Skeleton
cmds.button( label='Rig Weapon and Sheathe', command=('ButtonSkinWeapon()'))

# Take wSheathe, unbind it, translate it to world origin and point it down X to make the world mesh variant
cmds.button( label='Create Weapon World Mesh', command=('ButtonCreateWeaponWM()'))

# Export Hairs
cmds.button( label='Export Skeletal Asset', command=('ButtonExportSK()'))

# Export Meshes
cmds.button( label='Export Weapon', command=('ButtonExportWeapon()'))



# -------------------------------------------- Anim Thievery ---------------------------------------------- #
# next section header
cmds.text( label=' ', align='center' )
cmds.text( label='Anim Copying', align='center', fn="smallObliqueLabelFont" )
cmds.text( label=' ', align='center' )

# Read Joint Rotations from Epic Rig button
cmds.button( label='Orient to Epic Joints', command=('ButtonOrientEpic()'))

# Read Joint Rotations from Epic Rig button
cmds.button( label='Rig to Epic Joints', command=('ButtonCopyEpicPush()'))

# Read Joint Rotations from thirdparty horse pack button
cmds.button( label='Copy Horse Joints', command=('ButtonHorseCopyPush()'))



# -------------------------------------------- Animation Tools ---------------------------------------------- #
# next section header
cmds.text( label=' ', align='center' )
cmds.text( label='Animation', align='center', fn="smallObliqueLabelFont" )
cmds.text( label=' ', align='center' )

# Select aHuman Rig
cmds.button( label='Select Almerra Rig', command=('ButtonSelectAlmerra()'))

# Read Joint Rotations from Epic Rig button
cmds.button( label='Bake Anims', command=('ButtonBakePush()'))

# Read Joint Rotations from Epic Rig button
cmds.button( label='Export Anims', command=('ButtonExportPush()'))



# -------------------------------------------- Scene/Misc Tools ---------------------------------------------- #
cmds.text( label=' ', align='center' )
cmds.text( label='Misc Tools', align='center', fn="smallObliqueLabelFont" )
cmds.text( label=' ', align='center' )

# Read Joint Rotations from Epic Rig button
cmds.button( label='Import DMan', command=('ButtonImportDMan()'))

# Take wWeapon and wSheathe and rig them to Almerra Skeleton
cmds.button( label='Import Collider Proxys', command=('ButtonImportCollider()'))

# Take wWeapon and wSheathe and rig them to Almerra Skeleton
cmds.button( label='Export Geo', command=('export_geo()'))


# -------------------------------------------- World48 Tools ---------------------------------------------- #
cmds.text( label=' ', align='center' )
cmds.text( label='Map Tools', align='center', fn="smallObliqueLabelFont" )
cmds.text( label=' ', align='center' )

# Return the values of the input as integers for setting the level coordinates to load
# Should be run as what kind of size?
# 48 x 48 = the 9,699,742 world
# loading 8 realworld cells as one map cell atm so:
# 6 x 6 = the 11,597 worldmap
# 836.4009657 div
# worldmap is 0.0011955988 of world scale
def load_worldmap_cells():
    # Get the values from the integer input fields
    value1 = cmds.intField(intField1, query=True, value=True)
    value2 = cmds.intField(intField2, query=True, value=True)

    # Replace this with your custom script logic
    print("Load Worldmap Grid Cell: " + str(value1) + ' ' + str(value2))
    aCreateWorld48.run_import_world_loop(value1, value2)
    
# Geo Reduce 85%
def curate_cells():
    aReduceWorld48.reduce_objects_in_geo_group()

# Export Geo Relative only
def export_geo():
    aExportGeo.export_geo_as_fbx(True)

# Export Worldmap
def exportmap_cell():
    aExportGeo.export_worldmap_geo()

# Create two integer input fields
intField1 = cmds.intField(value=0)
intField2 = cmds.intField(value=0)



# Create a button to execute the scrip
cmds.button( label="Load 8x8 Map Coordinates", command=('load_worldmap_cells()'))

# Create a button to execute the scrip
cmds.button( label="Reduce Worldmap", command=('curate_cells()'))

# Create a button to execute the scrip
cmds.button( label="Export Worldmap", command=('exportmap_cell()'))

# Close button with a command to delete the UI
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )

# Set its parent to the Maya window (denoted by '..')
cmds.setParent( '..' )

# Show the window that we created (window)
cmds.showWindow( window )



#################################################### The goods ####################################################

# All button command links
def ButtonImportDMan():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aDMan.py")
    
def ButtonImportCollider():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aImportColliders.py")
    
def ButtonReadSkeleton():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\ReadSkeleton.py")
    
def ButtonCreateWeaponWM():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aCreateWM.py")

def ButtonSelectAlmerra():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aSelect.py")

def ButtonCopyRig():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aCopyRig.py")
    
def ButtonHorseCopyHorse():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aCopyHorse.py")
    
def ButtonOrientEpic():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aOrientToEpic.py")

def ButtonSkinScalp():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aSkinScalp.py")

def ButtonBake():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\Bake.py")

def ButtonExportAnim():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\ExportAnim.py")
    
def ButtonCleanHistory():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\CleanHistory.py")
    
def ButtonSkinWeapon():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aSkinWeapon.py")
    
def ButtonExportWeapon():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aExport_Weapon.py")
    
def ButtonExportSK():
    execfile(r"D:\UE4\Tailwind_R E B U I L D\Resources\Code\SimsMaya\aExport_SkeletalAsset.py")