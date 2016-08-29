REM # Edited Chad Parry's script to run on windwos:
REM # os.path.samefile not available on windows
REM def samefile(path1, path2):
REM     return os.path.normcase(os.path.normpath(path1)) == os.path.normcase(os.path.normpath(path2))

h:
cd H:\dev\LaggAt\LaggAt-Kodi\repo
python H:\dev\3rdParty\kodi-repo-script.chad.parry.org\tools\create_repository.py ..\src\repository.LaggAt ..\src\script.audioswitch
pause