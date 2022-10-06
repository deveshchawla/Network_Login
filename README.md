# Network_Login
Automates login for the MNIT Internet Access page

##Dependencies
>['requests'](https://pypi.org/project/requests/)
>['beautifulsoup4'](https://pypi.org/project/beautifulsoup4/)

##Note: Make sure you to set your login credentials in line 14 and 15 in login_script.py

--- 

##How to use the script
1. Go to the directory where the login_script is located.
2. Open terminal and type the command, python3 login_script.py

##Create a batch file and running a task scheduler
1. Create a batch file with the following commands
    cd "C:\Workspace" // path where your login_script is located
    start "" "path_to_your_python.exe" "login_script.py"
