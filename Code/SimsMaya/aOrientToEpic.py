import maya.cmds as cmds
import os

# Find the joint named "head" under the namespace "aHumanSkeleton"
joints = cmds.ls("aHumanSkeleton:hips", type='joint')
selectjoint = cmds.select(joints)