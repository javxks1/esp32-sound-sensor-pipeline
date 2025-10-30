# ESP32 Sound Data Pipeline (Streamlit Dashboard)
This project takes data from the ESP32 device and processes it into a dashboard using Streamlit. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 1. Project Structure
esp32-sound-pipeline  
analytics > Streamlit app  
ingestion > (scripts for ingestión)  
data > (CSV files o raw data)  
.venv  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2. Requisites
Windows 11/10  
Python 3.12   
ESP32 with Sound Sensor

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 3. Virtual enviroment

In PowerShell write the following:

py -3.12 -m venv .venv  
Create the environment in the same folder as your project. 

Note: Creating the enviroment in the same folder is very important since all dependencies will install here. If not, open powershell as an administrator, type cd "File path for downloaded project".

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 4. Activate it  

If you are in the folder path in PowerShell type the following: 

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 5. Dependencies
   
pip install --upgrade pip
pip install streamlit pandas numpy

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 7. Data Source (Sound)
Data can come in different ways for this project, the main one CSV files and by MQTT serial. A data 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 8. Dashboard
streamlit run analytics/streamlit_app.py

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 9. Errors might appear
ImportError: Erase the numpy folder or re-create environment. 
Fatal error while lanching: Re-create environment.
Blocked scripts: Use Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

[ESP32 Sound Live Dashboard](https://imgur.com/a/33wbRLL)
