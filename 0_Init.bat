@echo off
attrib -r "Z:\InProd\WoA\Jenkins\workspace\WoA_2702\Engines\Tailwinds_2702\Engine\Intermediate\Build\XmlConfigCache.bin"
call "Z:\InProd\WoA\Jenkins\workspace\WoA_2702\Engines\Tailwinds_2702\RunUAT.bat" BuildGraph -Script=Engine/Build/Graph/Examples/BuildEditorAndTools.xml -Target="Submit To Perforce for UGS" -set:EditorTarget=UE4Editor -set:ArchiveStream=//UE4/Dev-Binaries -p4 -submit uebp_PORT=192.168.50.146:1666 uebp_CLIENT="SimsLab_2702"
