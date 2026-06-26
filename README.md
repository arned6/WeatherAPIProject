# WeatherAPIProject
Install Project for App Engineer Interview

Prerequisites:
  1. Python 3.x
  2. pip (bundled with python 3.x)
  3. venv (bundled with python 3.x)
  4. local git

Install Instructions:
  1. Navigate in console to your Python Workspace
  2. In console, run command: ```git clone https://github.com/arned6/WeatherAPIProject```
  3. Path in terminal to your python project download for WeatherAPIProject (usually in root)
  4. Install .venv (not mandatory, but highly recommended to avoid packages being installed in global python environment)
     Windows:

     a. In cmd (pathed to the project folder) run command python -m venv .venv

      b. Activate venv with .venv\Scripts\activate.bat
     Mac:
       a. In terminal (pathed to the project folder) run command python3 -m venv .venv
       b. Activate venv with source .venv/bin/activate
  6. Install dependencies using commands pip install -r requirements.txt from the project folder
  7. Run main program:
     Windows: run command python main.py
     Mac: run command python3 main.py

Adding New Locations:
  1. Navigate to file config/config.json
  2. Add a new location using the following json structure:
   {"code":"XYZ,
    "latitude":"12.4567",
    "longitude":"123.456"   
   }
  3. Save and commit 
