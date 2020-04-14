# projectInitializer
Automate project creation using Python
#only on Windows Users

```
create env vars in your System:
> projects directory - "PROJ_PATH"
> Github token  - "GIT_TOKEN"
```

### setup: 
```bash
git clone "https://github.com/dibasbehera7/projectInitializer.git"
cd projectInitializer
pip install -r requirements.txt
touch .env
Then open the .env file and store your username, password, and desired file destination. Use the provided format at the bottom of this README.
source ~/.my_commands.sh
```

### Env File Format:
```bash
USERNAME="dibasbehera7"
PASSWORD="GIT_TOKEN"
FILEPATH="D:\DHub"
```


### Usage:
```bash
To run the script type in 'create <name of your folder>'

'create <project_name> <g>'   - for local + git
'create <project_name> <l>'   - for just locally
```
