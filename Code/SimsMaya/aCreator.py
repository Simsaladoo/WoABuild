import maya.cmds as cmds

# Function to execute when the button is pressed
def execute_script(*args):
    # Get the values from the integer input fields
    value1 = cmds.intField(intField1, query=True, value=True)
    value2 = cmds.intField(intField2, query=True, value=True)

    # Replace this with your custom script logic
    result = value1 + value2
    print(f"Result of the operation: {result}")

# Create a window
window_name = "myUIWindow"
if cmds.window(window_name, exists=True):
    cmds.deleteUI(window_name)

cmds.window(window_name, title="My UI Window", widthHeight=(300, 100))

# Create two integer input fields
intField1 = cmds.intField(value=0)
intField2 = cmds.intField(value=0)

# Create a button to execute the script
cmds.button(label="Execute", command=execute_script)

# Show the window
cmds.showWindow(window_name)
