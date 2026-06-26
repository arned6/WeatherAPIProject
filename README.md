# WeatherAPIProject
Install Project for App Engineer Interview


## Setup and Run Instructions

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

## Design Decisions and Justifications

### Class Control
  The WeatherAPI, Meteostat and templates for our api providers were designed as individual classes with separate .py files for each. This was to allow for synchronous changes that would only affect individual API providers; additionally, this allowed for easier parallel processing using ThreadPoolExecutor. 

  the Provider Template was created with the variables required for altering made clear. This, combined with the .env file and the preexistence of the class for tempalting, should allow for the adding of a new API by only editing the Class variables, the api parameters required by the host, and the class call within the main file.

### API Key and Variable Storage
  A .env file was created to include variables for APIs that are not hardcoded into the source. This is best practice for programming with APIs. In a live environment with paid keys, our API variables would be hosted in secret (usually using AWS or gitignore) but I kept them available to the project for ease of transferring.

### Location Storage and Configuration
  All Locations are stored in a config.json file for ease of editing without requiring editing of the source code. Along with this, I decided to implement location validation and selection for the user; with this in mind, not only can the user add locations without touching the source code, the code will also dynamically pick them up, add them to an input list at the beginning of the application, and allow for selection. I included recursion on the airport selection functionn that will cause the program to loop until a valid selection is chosen.

### Reporting
  The code for the reporting output engine (Lines 13-48 of reportingengine.py) was created almost entirely by AI with adjustments by the engineer for proper dictionary calling and security validation. It is designed so that weather data from any API can be plugged into it, so long as that weather data contains the same parameters as what are called for in the comparison report.

# Assumptions

-APIs are stored in the .env file securely
-User understands basic knowledge of CLI usage and knows how to install git, python, etc
-All APIs used by this program will require latitude, longitude and date. I built start and end date into the API paramaters by calling the date variable twice in case this is needed by a future API.
-All data needs to be normalized to imperial standards
-Date timestamps need to be normalized to YYYY-MM-DD
-Only daily aggregations are used
-Drift is calculated absolutely, not by percentage
-Each provider responds using JSON and is REST based 

## Future Improvements
Given more time and a large scope, I would include the following improvements:
 1. Cloud storage of API keys for security
 2. GUI Interface, incuding:
    1. The ability to add location via text boxes
    2. Loading of the .csv report directly into the UI
    3. Dropdown selection of Weather APIs as they are added
 3.Better exception handling & edge case prevention (for example, what happens if one provider fails to respond)
 4. Cloud storage of CSV data
 5. Coded rules for validation
 6. API integration for airport code lat/lon for ease of use
 7. logged API handling errors
 8. rate limiting warnings
 9. Dynamic drift report warnings based on affected data parameters
