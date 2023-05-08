# Tennis Twine (Han Solo Servers)

## Hacklahoma 2023 Project by Luke Sparlin and Joshua Hooper
- Created in VS Code with inspiration from these tutorials:
- https://code.visualstudio.com/docs/python/tutorial-flask
- https://flask.palletsprojects.com/en/2.2.x/tutorial/

## Setup Instructions:
1. Clone the repository
2. Make the Python virtual environment (inside the project folder) then activate it
   - On Mac/Linux:
     - `python3 -m venv venv`
     - `. venv/bin/activate`
   - On Windows:
     - `py -3 -m venv venv`
     - `venv\Scripts\activate`
3. Install the required Python libraries from the included requirements file
   - `pip3 install -r requirements.txt`
4. Set environment variable FLASK_APP to flaskapp
   - On Mac/Linux: 
     - `export FLASK_APP=flaskapp`
   - On Windows: 
     - `set FLASK_APP=flaskapp` (CMD)
     - `$env:FLASK_APP="flaskapp"` (Powershell)
5. Initialize the SQLite database
   - `flask init-db`
6. Start the application
   - `flask run`