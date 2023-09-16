print("Running Rig Hair")

import maya.cmds as cmds

# Refs
all_objects = cmds.ls()
hair_geo = []
selectgeo = []
skinCluster = ''


# Find the joint named "head" under the namespace "aHumanSkeleton"
joints = cmds.ls("aHumanSkeleton:head", type='joint')
selectjoint = cmds.select(joints)



# Find all hair geometry under the "Geo" group
geo_group = cmds.ls('Geo', g=True)
selectgeo = cmds.select('aHair_*', 'aScalp_*')
selected_shapes = cmds.listRelatives(selectgeo, shapes=True)



for shape in cmds.ls(type='mesh'):
    print("Selected: {}".format(shape))
    if shape:
        Clustername = shape + '_SC'
        skinCluster = cmds.skinCluster(joints, shape, name=Clustername)
        
        print("Creating skin for: {}".format(shape))
        if skinCluster:
            print("Weighting skin for: {}".format(skinCluster))
            cmds.skinPercent(Clustername, shape, transformValue=[("aHumanSkeleton:head", 1.0)])



