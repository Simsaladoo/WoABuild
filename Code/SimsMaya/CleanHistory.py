import maya.cmds as cmds
import maya.mel as mel



    # our functions for the button conections. If we just put the cmd in the
    # clicked.connect function, it would call it when we open the Ui
def delHist(self):
    mel.eval("DeleteAllHistory")


def delNonDefHist(self):
    mel.eval("BakeAllNonDefHistory")
