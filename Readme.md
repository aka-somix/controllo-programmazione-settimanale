# Controllo Programmazione Settimanale
## Summary  
A simple app to automate some checkings for correctness into an excel file (.xlsx).


## IMPORTANT - Documentation
As this is just an Alpha version, full documentation is still in progress and may not ever be delivered.


### What do i need to start
This project is entirely based on **Python 3.x**.  
To start the application on your local machine you may want first to set up the pipenv environment with
```
pipenv install
```
and then just run
```
pipenv run python app.py
```

else, you can install the dependencies listed in the PipFile by yourself using pip or whatever other similar tool you like.

### Building the app
This project leverages *pyinstaller* for building the desktop app for Windows.
A file *.spec* is already defined, so you can run:

```
pipenv run pyinstaller ps-check.spec
```

or, if you don't use pipenv, you can simply run
```
pyinstaller ps-check.spec
```


# CHANGELOG
Version number is updated in the \_\_init\_\_.py file inside modules folder. 

**[ALPHA1.2.0]**  
- *Added*
  - Improved Graphic 
- *Changed*
  - Full day check of errors

**[ALPHA1.0.0]**  
- *Added*
  - Data extraction Business logic
  - Error check in morning and afternoon shifts
  - GUI 