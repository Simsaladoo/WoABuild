from P4 import P4, P4Exception
import os
import filecmp
import shutil
from datetime import datetime

## pywin32 same codebase as robomirror
import win32com.client

art_source_dir = 'D:/UE4/Tailwind_R E B U I L D'
game_source_dir = 'D:/UE4/Engines/Tailwinds_2702/Projects'
target_art_dir = 'Z:/InProd/WoA/SimsLab_2702/Tailwind_R E B U I L D'
target_game_dir = 'Z:/InProd/WoA/SimsLab_2702/Engines/Tailwinds_2702/Projects'
null_dirs = ['Saved', 'Intermediate', 'DerivedDataCache', 'Build/', 'AssetRegistryCache']
null_types = ['.pyc', '.code-workspace']
changelist_dir = 'Z:/InProd/WoA/Code/SyncLogs/'

    
def submit_dailies():
    ''''''
    # Generate the changelist log file name based on the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    changelist_file = changelist_dir + 'SimsSync_' + timestamp + '.txt'
    print('Creating new changelist sync file: ' + changelist_file)
    
    # Create or open the changelist file for logging differences
    with open(changelist_file, 'w') as log_file:
        phase1_time = datetime.now().strftime("%Y-%m-%d, " + "%H:%M:%S")
        print('Preparing to submit daily art source changes: ' + phase1_time)
        compare_and_update(changelist_file, log_file, art_source_dir, target_art_dir)
        
        phase2_time = datetime.now().strftime("%Y-%m-%d, " + "%H:%M:%S")
        print('Preparing to submit daily game engine changes: ' + phase2_time)
        compare_and_update(changelist_file, log_file, game_source_dir, target_game_dir)
             
    finish_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    total = elapsed(timestamp, finish_time)
    print('Changes logged...' + ' Elapsed Time: ' + str(total))
    
    
def create_dir(output):
    ''''''
    missing_dir = os.path.dirname(output)
    # os.makedirs(missing_dir, exist_ok=True)
    print('Created new dir: ' + missing_dir)

def copy_file(input, output):
    ''''''
    # shutil.copy2(input, output)
    
# sync the file
def submit_file(input, output): 
    ''''''
    print(output)
    if os.path.exists(output):
        ## Copy command
        copy_file(input, output)
        print('Updated ' + output + ' with ' + input)
        
        
    else:
        # we need to make the dir before we can copy
        missing_dir = os.path.dirname(output)
        print('Path does not exist: ' + output)
        create_dir(output)
        copy_file(input, output)
        print('Updated ' + output + ' with ' + input)

    
    
def elapsed(start, end):
    ''''''
    # Convert the input timestamps to datetime objects
    start_time = datetime.strptime(start, "%Y%m%d_%H%M%S")
    end_time = datetime.strptime(end, "%Y%m%d_%H%M%S")

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    return elapsed_time
    
    
    
def compare_files(input, output): 
    ''''''
    # True means no need to copy, up to date
    size1 = os.path.getsize(input)
    size2 = os.path.getsize(output)
    
    # compare size
    if size1 == size2:
        ''''''
        return True
    
    # files are different, so copy
    else:
        # print('Size mismatched: ' + str(size1) + ' =/= ' + str(size2))
        return False
    
    
def check_ignored_types(filetype):
    ''''''
    bFound_an_Ignore = False
    
    for ignored in null_types:
        if ignored in filetype:
            bFound_an_Ignore = True
            # print('Ignores check found ignored type: ' + filetype)
            
    return bFound_an_Ignore

    
    
def check_ignored_folders(path):
    ''''''
    bFound_Ignore = False
    
    for folder_ignore in null_dirs:
        if folder_ignore in path:
            bFound_Ignore = True
            # print('Ignores check found ignored path: ' + path)
            
    return bFound_Ignore

        
        
def check_ignores(path, type):
    ''''''
    if check_ignored_folders(path) or check_ignored_types(type):
        return False
    else:
        return True
    
    
# runs comparisons and write the output to supplied log
def compare_and_update(changelist_file, log_file, input_dir, output_dir):
    ''''''
    # Compare the input and output directories
    dcmp = filecmp.dircmp(input_dir, output_dir)
    log_file.write(f"Changelist for comparing '{input_dir}' and '{output_dir}':\n\n")
    
    # Recursively compare files in the directories
    for dirpath, dirnames, filenames in os.walk(input_dir):
        for filename in filenames:
            if check_ignores(dirpath, filename):
                # for each ignored filetype in list        
                input_file_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(input_file_path, input_dir)
                output_file_path = os.path.join(output_dir, relative_path)
                          
                if os.path.exists(output_file_path):
                    if compare_files(input_file_path, output_file_path):
                        # ignores when filesize A==B
                        # print('Up to date: ' + dirpath + ', ' + filename)
                        ''''''
                    else:
                        log_file.write(f"Difference found in File: {relative_path}\n")
                        submit_file(input_file_path, output_file_path)
                        log_file.write(f"Updated '{output_file_path}' with '{input_file_path}'\n\n")              
                                
                else:                      
                    log_file.write(f"Adding New File: {relative_path}\n")
                    submit_file(input_file_path, output_file_path)

            else:
                ''''''
                # print('Check Ignores False: ' + dirpath + ', ' + filename)
            
        
    log_file.write("---End of Changelist---"'\n\n')


def submit(p4, _Input):
    print("SimsLab: Syncing latest editor changes..." + _Input)
    # fetch gives us the dict of the current default changelist
    p4.run("sync", _Input)



# Reconcile offline work on the specific folder and its descendants 
def sync_changes(p4, _Input, _Workspace):
    # Set the client workspace to reconcile offline work
    p4.client = _Workspace
    submit(p4, _Input)



def submit_p4_changes():
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
            sync_changes(p4, "//WoAStream/WoA_mainline/Engines/Tailwinds_2702/Projects/...", "jenkins-jenkins")

        else:
            print("SimsLab: Connection to Perforce server failed!")

    except P4Exception as e:
        print(e)

    finally:
        p4.disconnect()
        print("SimsLab: Disconnecting from perforce")
        
        

        
submit_p4_changes()