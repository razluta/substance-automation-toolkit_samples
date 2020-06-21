@echo off

echo Processing, please wait ...
echo ...

set source-meshes-path=sources.txt
for /f "tokens=*" %%p in (%source-meshes-path%) do (
    for /f "tokens=1,2 delims= " %%a in ("%%p%") do (
        echo Source: %%a
        echo Target: %%b
        echo Baking ...

        :: Section 01 of 02
        :: If you installed the Substance familly of the tools in the default location, skip to Section 02
        :: If not, replace the "C:" with your drive and the path after "cd" with your own path ...
        :: ... to the Substance Automation Toolkit directory/folder      
        C: >nul
        cd "C:\Program Files\Allegorithmic\Substance Automation Toolkit" >nul

        :: Section 02 of 02
        :: This is the full command for baking bent normals using the Substance Automation Toolkit command line
        sbsbaker.exe bent-normal-from-mesh ^
        --inputs "%%a" ^
        --highdef-mesh "%%b" ^
        --output-path "C:\bakes\output_folder" ^
        --output-name "{inputName}_BN" ^
        --output-format png ^
        --output-size 12,12 ^
        --antialiasing 0 ^
        --ignore-backface true ^
        --self-occlusion 0 ^
        --use-lowdef-as-highdef false ^
        --uv-set 0

        echo Finalized Bent Normal bake for %%a
        echo -----
    )
)

echo All bakes are done!
pause