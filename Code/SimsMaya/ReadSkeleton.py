import pymel
from maya import cmds


joints = []

def ReadJoints():
    """ Returns the Rotation for each joint """
    jointsList = pymel.ls(type="root")

    cmds.select(jointsList)
    selected = cmds.ls(selection=True)

    if len(jointsList):

        print("No joints found")

    if not len(jointsList):
        for i in jointsList:
            joints.append(i)
        for j in joints:
            m1 = cmds.getAttr(j+'.rotateX')
            m2 = cmds.getAttr(j+'.rotateY')
            m3 = cmds.getAttr(j+'.rotateZ')
            ms1 = str(m1)
            ms2 = str(m2)
            ms3 = str(m3)
            output1 = j + ' Rotate X = ' + ms1
            output2 = j + ' Rotate Y = ' + ms2
            output3 = j + ' Rotate Z = ' + ms3
            print(output1 + output2 + output3)



ReadJoints()

