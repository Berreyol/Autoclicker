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
there is a pipfile inside the project folder. Type in the command line the following to install autoclicker libraries:
```
pipenv shell
pipenv sync
```
Now you can execute the autoclicker without problems
``` python3 main.py ```

***You don't need to be in console to perform above instructions so watch out if you pressing any key anywhere, the autoclicker will respond to it***


#### Instructions:
- Press 'f2' to star recording your clicks and movements
- Press 'f2' to stop recording
- Press 'r' to input the number of times the record will be perform. **By default the recorder will execute just one time.**
- Press 'f3' if you want to add interval between records
- **Press 'f1' to start the autoclicker**
- Press 'f2' if you want to stop the autoclicker
- Press 'f4' to exit the application

**If you stop and resume the autoclicker the recorder will no start over, indeed will keep clicking where the cursor was stopped previously**
