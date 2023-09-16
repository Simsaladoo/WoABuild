import os
import subprocess
import datetime


unrealContentDir = r'D:\UE4\Projects\WoA_2403\Content'
ZeeDir = r'Z:\InProd\WoA'
ffmpeg = r"Z:\InProd\WoA\Code\ffmpeg-master-latest-win64-gpl\bin"
RenderArena = r"Z:\InProd\WoA\editorial\footage"

## All Rendering projects
RACineFlags = "CineBackstories\CineFlags"
RAIntro1 = "Intro1"
RAIntro2 = "Intro2"
RAMoneyshots = "Moneyshots"
RANationcards = "Nationcards"
RAPrologue = "Prologue"

## 3 for Moneyshots
inttrack = 3
Projects = [RACineFlags, RAIntro1, RAIntro2, RAMoneyshots, RANationcards, RAPrologue]



def postrenderMoneyshots():
    print('Looking For Frame Folders to Render...' + RenderArena + '/' + Projects[inttrack])
    
    for root, dirs, names in os.walk(RenderArena + '/' + Projects[inttrack], topdown=False):
        for names in dirs:
            ##print(str(names))
            if names.startswith('Flag'):
                print(names)
                thisShot = RenderArena + '/' + Projects[inttrack] + '/' + names
                derp = os.stat(thisShot).st_mtime 
                
                CheckDate(thisShot)
                
            if names.startswith('LS'):
                print(names)
                thisShot = RenderArena + '/' + Projects[inttrack] + '/' + names
                CheckDate(thisShot)
                derp = os.stat(thisShot).st_mtime
                
                
                
        
        
    ## the command:
    # ## ffmpeg 
    # ## -i 
    # ## "Z:\InProd\avastars\editorial\footage\Episodes\MUSIC VIDEO JIMMY_DAVINA\MV_JC_AVAWORLD_TK02_AR.mov" 
    # ## -r 50 -s 568x320 -framerate 50 
    # ## -f image2 "Z:/InProd/avastars/artists/dmiller/MusicVideo/_Frames/MV_JC_AVAWORLD_TK02_AR/MV_JC_AVAWORLD_TK02_AR_000%0d.png"

    


def CheckDate(checkShot):
    ## add date ranges all to relevant list
    for root, dirs, names in os.walk(checkShot, topdown=False):
        for names in dirs:
            os.path.dirname(names)
            outstats = str(names).split('.')
            outDay = outstats[2].split('_')


            
            print('Rendered Version: ' + str(names) + ', Date: ' + outstats[0] + ', Month: ' + outstats[1] + ', Day: ' + outDay[0] + ', Hour: ' + outDay[1])
            




            


            
    ## newRenderable = ''
    ## AllRenderables.append(newRenderable)
    ## print ("Latest for Render: " + str(AllRenderables))
    ## RenderVideo(newRenderable)
            

    






def RenderVideo(newRenderable):
    
    ## add output info to newRenderable
    
    commands = 'ffmpeg -i "Z:\InProd\WoA\editorial\footage\Moneyshots\LS_0010\2023.02.27_06.55.57\LS_0010.%03d.png" -framerate 30 "Z:\InProd\WoA\editorial\footage\Moneyshots\LS_0010"'
    print('Rendering Video: ' + commands)
    ## newRenderable is the input
    
    ##if subprocess.run(commands).returncode == 0:
        ##print ("FFmpeg Script Ran Successfully")









postrenderMoneyshots()                