# Autoclicker

## A simpe console autoclicker in python

#### Recuriments
- pynput or
- pipenv

**Using pypnput**
Just install pynput using pip
```
pip install pynput
```

**Using pipenv**
inside the project folder is a pipfile. Type in the command line the following to install the autoclicker dependencies:
```
pipenv shell
pipenv sync
```
Now you can execute the autoclicker without problems

#### Instructions:
- Press 'f2' to star recording your clicks and movements
- Press 'f2' to stop recording
- Press 'r' to input the number of times the record will be perform.
- Press 'f3' if you want to add interval between records
- Press 'f2' if you want to stop the autoclicker
- Press 'f4' to exit the application

**By default the recorder will execute just one time. press 'r' to update this value**

**If you stop and resume the autoclicker the recorder will no start over, indeed will keep clicking where the cursor was stopped previously**
