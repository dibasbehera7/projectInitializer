#locally creating project
# Make sure pre-installed: Git , Visual Studio Code

import os
import sys

folderName = str(sys.argv[1])
path = os.environ.get('PROJ_PATH') # var in System Environment
_dir = path + '/' + folderName #create a directory path

try:
    #creating a directory and getting into master directory
    os.mkdir(_dir)
    os.chdir(_dir)
    
    #intializing git to project : in case need to push project into github
    os.system('git init')
    #os.system(f'echo "# {folderName}" > README.md') issue
    os.system("echo # "+(folderName)+" > README.md") #fix #insert some initial comment into file
    os.system('git add README.md')
    os.system('git commit -m "initial commit"')
    
    print(folderName+" created locally") #fix #getting information as it sucessfully created.
    #print(f'{folderName} created locally') issue
    os.system('code .') #open project in visual studio

except:
    print("create command fails : "+folderName+" is already exists.")

