import sys
import os
from github import Github

foldername = str(sys.argv[1])
path = os.environ.get('PROJ_PATH')         # add projects dirctory to the env vars
token = os.environ.get('GIT_TOKEN')        # add github token to the env vars
_dir = path + '/' + foldername

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername)


commands = ["echo # " +str(repo.name)+" >> README.md",
            'git init',
            "git remote add origin https://github.com/"+str(login)+"/"+str(foldername)+".git",
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

# print("args :"+str(sys.argv[0])+" - "+str(sys.argv[1])+" - "+str(sys.argv[2]))
if sys.argv[2] == "g":
    os.mkdir(_dir)
    os.chdir(_dir)

    for c in commands:
        os.system(c)

    print(str(foldername)+" created locally")
    os.system('code .')

else:
    print("create <fldername> command fails: "+str(foldername)+" already exsits or credentials fails to authenticate by GitHub API...")
