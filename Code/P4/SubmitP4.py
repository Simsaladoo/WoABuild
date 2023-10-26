
from P4 import P4, P4Exception
import os


# Reconcile offline work on the specific folder and its descendants 
def Reconcile(p4, _Input, _Workspace):
    # Set the client workspace to reconcile offline work
    p4.client = _Workspace
  
    # fetch gives us the dict of the current default changelist
    change = p4.fetch_change()
    
    # not adding to our selected chagnelist--goes into default
    # clNum = p4.save_change(change)[0].split()[1]
    
    p4.run_reconcile(_Input, '-e', '-a', '-d')
    description = _Workspace + ": [Jenkins]: Submitting offline changes"
    result = p4.run_submit('-d', description)
    


def submit_changes(directory, workspace):
    print("SimsLab: Creating read object...")
    p4 = P4()

    print("SimsLab: Setting workspace configs")
    # Connect to the Perforce server
    p4.port = "192.168.50.146:1666"
    p4.user = "Simsaladoo"

    try:
        print("SimsLab: Attempting to connect to Perforce server...")
        p4.connect()

        if p4.connected():
            print("SimsLab: Connection to Perforce server is running!")   
            Reconcile(p4, directory, workspace)

        else:
            print("SimsLab: Connection to Perforce server failed!")

    except P4Exception as e:
        print(e)

    finally:
        p4.disconnect()
        print("SimsLab: Disconnecting from perforce")
        
        
def submit():
    print("SimsLab: Running art source submit...")
    submit_changes("//WoAStream/WoA_ArtSource/Tailwind_R E B U I L D/...", "SimsLab_2702_Art")
    
    #print("SimsLab: Running editor files submit...")
    submit_changes("//WoAStream/WoA_mainline/Engines/Tailwinds_2702/Projects/...", "SimsLab_2702")
        
        
        
# Autorun for jenkins     
submit()
print("SimsLab: Submit Finished")
