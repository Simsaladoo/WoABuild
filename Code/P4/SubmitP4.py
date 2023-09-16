import P4

p4 = P4.P4()

# Connect to the Perforce server
p4.port = "192.168.50.146:1666"
p4.user = "Simsaladoo"
print("SimsLab: Running Full P4 Submit")


def Reconcile(_Input):
    # Set the client workspace to reconcile offline work
    p4.client = "Simsaladoo_mainline"

    # Reconcile offline work on the specific folder and its descendants
    p4.run_reconcile("-w", _Input)
    change = p4.fetch_change()
    change["description"] = "SimsLab: [Automation]: Submitting offline changes"
    p4.run_submit(change)
    
    
    
    
    


def CheckRunning():
    try:
        p4.connect()

        if p4.connected():
            print("SimsLab: Connection to Perforce server is running")
            
            print("SimsLab: Running Reconcile for Art Source...")
            Reconcile("//WoAStream/WoA_mainline/Tailwind_R E B U I L D/...")
            
            print("SimsLab: Running Reconcile Project...")
            Reconcile("//WoAStream/WoA_mainline/Engines/Tailwinds_2702/Projects/...")
        else:
            print("SimsLab: Connection to Perforce server is not running")

    except P4.P4Exception as e:
        print(e)

    finally:
        p4.disconnect()
        
        
        
CheckRunning()



print("SimsLab: Submit Finished")
