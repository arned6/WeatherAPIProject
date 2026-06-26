1. User runs main.py file
2. User input asks for an airport code, exception handles for failed inputs
    2a. The console will provide a list of codes available
3. Do Work
    3a. main.py will pull the latitude and longitude from the config file, and input latitude, longitude and start/end date into the api call header
    3b. api header will GET data from website handler a and handler b classes
    3c. this is pulled back into main.py, which feeds key data into normalizer
    3d. normalizer feeds normalized data into comparator function (once for each data set)
    3e. comparator function compares data a and data b, measures it and identifies configuration drift
    3f. data information is piped into reporting module and injected into a .csv file
4. Console will loop back to input field
