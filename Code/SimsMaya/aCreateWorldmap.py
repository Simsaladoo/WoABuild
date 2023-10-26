import os
import maya.cmds as cmds
import datetime

Target_Ma = 'D:/UE4/Tailwind_R E B U I L D/Worldmap/WorldmapActor/World48_Landmesh'

class LoopBreakException(Exception):
    print("Command Exception")
    pass

# Function to perform a 50% polyReduce on a given object
def perform_poly_reduce(obj):
    # Select the object
    cmds.select(obj)
    cmds.polyReduce(version=1, keepQuadsWeight=0.5, percentage=70)

# Function to loop through all objects in the "Geo" group and reduce them
def reduce_chunks():
    # Check if the "Geo" group exists
    if cmds.objExists("Geo"):
        # List all objects in the "Geo" group
        geo_group_objects = cmds.listRelatives("Geo", children=True, fullPath=True)

        # Loop through each object and perform polyReduce
        for obj in geo_group_objects:
            perform_poly_reduce(obj)
            cmds.delete(obj, constructionHistory=True)
    else:
        print("The 'Geo' group does not exist in the scene.")


def get_worldmap_actor_group(input):   
    group_search_pattern = cmds.ls(input)
    if cmds.objExists(input):
        print("Found existing group: " + input)
        return group_search_pattern
    else:
        cmds.group(em=True, name=input)
        print("Created new group: " + input)
        return group_search_pattern
    

def save_import_phase(file_count):
    # Save the scene with a new name if needed.
    construction_path = 'Z:/InProd/WoA/Dev/Worldmap/chunks'
    ma_file_path = construction_path + '/' + 'World48_Landchunks_' + str(file_count)
    cmds.file(rename=ma_file_path)
    cmds.file(save=True, type="mayaAscii")

  
  
def reparent_chunk(chunk_group):
    if cmds.objExists('Geo'):
        # List all objects in the "Geo" group
        geo_group_chunks = cmds.listRelatives("Geo", children=True, fullPath=True)
        # Loop through each object and perform polyReduce
        for chunks in geo_group_chunks:
            cmds.parent(chunks, chunk_group)
         
    
def scale_chunks(group):
    scale_group = group 
    if cmds.objExists(group):
        # Scale down new group
        print('Scaling objects in group: ' + str(scale_group))
        
        scale_factor = 0.001
        cmds.scale(scale_factor, scale_factor, scale_factor, scale_group) 
        # geo_group_objects = cmds.listRelatives(scale_group, children=True, fullPath=True)
        
           
def group_chunks(file_base_name):
    # Create a group with the same name as the file, & add new grouping to base group
    new_group = file_base_name
    
    if not cmds.objExists(new_group):     
        print('Creating new group: ' + str(new_group))
        cmds.group(em=True, name=new_group) 
        # Move the cleaned Geo into the new group heierarchy
        cmds.parent(new_group, 'Worldmap_Actor')
        
        geo_group_chunks = cmds.listRelatives(new_group, children=True, fullPath=True)
        for geo_chunk in geo_group_chunks:  
            cmds.select(geo_chunk)  
        cmds.polyUnite(ch=True, mergeUVSets=1, centerPivot=1)
        
    reparent_chunk(new_group)
        
    
def chunk_import(new_load, dirpath, file_count):
    source_base_name = str(new_load).replace(dirpath, '').replace('\\', '').replace('.fbx', '')
    source_base_name = source_base_name + '_chunk'
    cmds.select(clear=True)
    # Select the Geo group contents and run polyReduce
    
    if check_chunk(source_base_name):
        cmds.file(new_load, i=True, type="FBX", rpr="FBX")
        reduce_chunks()

        ## Create hierarchy
        group_chunks(source_base_name)    
        scale_chunks(source_base_name)

        cmds.file(rename=Target_Ma)
        cmds.file(save=True, type="mayaAscii")
        print("Scene re-saved:", Target_Ma)

        # Save intermediate ma file
        save_import_phase(file_count)
        
        raise LoopBreakException()
    
    
# Ensure we haven't already imported this group
def check_chunk(source_base_name):
    if cmds.objExists(source_base_name):
        return False
    else:
        return True
    
      

def import_map_chunkes():
    base_group = get_worldmap_actor_group('Worldmap_Actor')
    
    ## ('New Construct Timestamp: ', '2023-10-20 12:27:40.257000')
    timestamp = str(datetime.datetime.now())
    print("New Construct Timestamp: ", timestamp)
    
    # Directory where .fbx files are located
    directory_path = 'D:/UE4/Tailwind_R E B U I L D/Worldmap/WorldmapActor/Worldchunks'
    fbx_files = []
    reversed_fbx_list = []
    file_count = 0
    
    for filename in os.listdir(directory_path):
        if str(filename).endswith('.fbx') and not str(filename).endswith('.txt'):
            fbx_file_path = os.path.join(directory_path, filename)
            fbx_files.append(fbx_file_path)
            
    for file in fbx_files:
        reversed_fbx_list.append(file)
        print('Found exported Landscape: ' + str(file))


    # Step 5: For each .fbx file, import it, create a group, and run polyReduce.
    for fbx_file in reversed_fbx_list:
        new_load = str(fbx_file)
        print('loading: ' + new_load)
        chunk_import(new_load, directory_path, file_count)
        file_count = file_count + 1
        

    