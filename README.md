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
     1. In cmd (pathed to the project folder) run command ```python -m venv .venv```
     2. Activate venv with command ```.venv\Scripts\activate.bat```    
     
     Mac:
       1. In terminal (pathed to the project folder) run command ```python3 -m venv .venv```
       2. Activate venv with source ```.venv/bin/activate```
  
  6. Install dependencies using command ```pip install -r requirements.txt``` from the project folder
  7. Run main program:

     Windows: run command ```python main.py```

     Mac: run command ```python3 main.py```

Adding New Locations:
  1. Navigate to file config/config.json
  2. Add a new location using the following json structure:
   {"code":"XYZ,
    "latitude":"12.4567",
    "longitude":"123.456"   
   }
  3. Save and commit

Adding a new API Provider:
  Adding a new API provider to the application requires knowledge of the vendor's API calls & headers. Please thoroughly consult your documentation prior to attempting this. 
  1. Add an API URLS and keys to /.env.
  2. Navigate to file providers/providertemplate.py.
  3. Comments are notated within the class - uncomment the code and replace all CAPPED variables with information from your vendors API documentation. This should include:
       1. Headers
       2. outputted key parameters for temperature, wind speed, humidity, etc
       3. URLs & API keys
  4. Lines 50-65 of main.py contain API provider objects based on their respective classes. You will need to replace any references to MeteoStat and WeatherAPI with your chosen provider.


Obtaining Outputs:
  1. Drift reports can be found in the file outputs/output.csv. 
