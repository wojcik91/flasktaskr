# flasktaskr

A simple to-do list tracking web app made for the RealPython web dev course. Certainly still work in progress.

## Usage
To start the app go to the main folder and activate the virtual environment:
```bash
source env/bin/activate
```
If it's the first time running the app you have to initialize the database:
```bash
python db_create.py
```
Then run the script:
```bash
python run.py
```
The app should be available in your browser at localhost:5000/

## Built with
* [Flask](http://flask.pocoo.org/)
