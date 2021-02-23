# PythonSensorView

[![Python application](https://github.com/jwupf/pythonSensorView/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/jwupf/pythonSensorView/actions/workflows/python-app.yml)

I hope that the code in the repo becomes something that reads, processes and presents sensor data.

The current plan is to run this code on a RaspberryPI B(no +), because it is collecting dust ...

The sensors will be controlled by micro controllers that do the initial (raw) data collection, but no processing. 
The data is then transfered to the Raspi this program runs on. 
The data is stored in some kind of database/file. 
Every time new data is available it will be processed and the results are stored, too. 
If a user wants to have a look, he connects to a webserver running on the Raspi. 
The data then will be presented in HTML, CSV or JSON format.
