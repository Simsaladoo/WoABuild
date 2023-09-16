import os
import subprocess



## -run=pythonscript -script="c:\\my_script.py"
scriptsed = ' -run=pythonscript '
scriptruntx = '-script='
scriptrun = r'"D:\UE4\Engines\Tailwinds_2702\Projects\WoA_2702\Content\Python\RenderPipeline.py"'
Project = r'D:\UE4\Engines\Tailwinds_2702\Projects\WoA_2702\WoA_2702.uproject'
EditorCMD = r'D:\UE4\Engines\Tailwinds_2702\Engine\Binaries\Win64\UE4Editor.exe'

commands = EditorCMD + ' ' + Project + scriptsed + scriptruntx + scriptrun
def RunEditor():
    if subprocess.run(commands).returncode == 0:
        print (commands)
    
    
    
RunEditor()