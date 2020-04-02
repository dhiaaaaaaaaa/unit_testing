# 
This Flask application contains the basic user management functionality (register, login, logout) 

#install requitements
 pip install -r requirements.txt

#Run the app 
 Unix Bash (Linux, Mac, etc.):
$ export FLASK_APP=hello
$ flask run
Windows CMD:
> set FLASK_APP=hello
> flask run

 # Unit Tests: I used a testing framework called "pytest"
 
- Test creating a new User (check email, check not plaintext password, check registration date, check is_authenticated is false)
- Test verifying the password for a User
- Test changing the password for a User and then verifying the password for that User
 *** you can run tests through the command 
 > pytest ; it will automatically find the test files and execute them
