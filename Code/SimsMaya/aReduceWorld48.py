import maya.cmds as cmds

# Function to perform a 50% polyReduce on a given object
def perform_poly_reduce(obj):
    # Select the object
    cmds.select(obj)

    # Perform a 50% polyReduce
    cmds.polyReduce(version=1, keepQuadsWeight=0.5, percentage=85)

# Function to loop through all objects in the "Geo" group and reduce them
def reduce_objects_in_geo_group():
    # Check if the "Geo" group exists
    if cmds.objExists("Geo"):
        # List all objects in the "Geo" group
        geo_group_objects = cmds.listRelatives("Geo", children=True, fullPath=True) or []

        # Loop through each object and perform polyReduce
        for obj in geo_group_objects:
            perform_poly_reduce(obj)
    else:
        print("The 'Geo' group does not exist in the scene.")

# Call the function to reduce objects in the "Geo" group
reduce_objects_in_geo_group()
