@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "error executing  %0 command : Please enter project name wisely"
) else ( 
    if "%2" == "" (
        echo "error executing  %0 %1 command : Please enter locally(l) or globally(g)"
    ) else (
        if "%2"=="g" (python remote.py %fn% %flag%) else (
            if "%2"=="l" (python local.py %fn% %flag%) else (
                echo "%0 %1 %2 command fails: Please enter locally(l) or globally(g)")) 
        )
    )

