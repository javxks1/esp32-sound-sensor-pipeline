@echo off
REM === Ir a la carpeta del proyecto ===
cd /d "C:\Users\sanch\Desktop\Data Engineering Projects\esp32-sound-temp-pipeline"

REM === Activar el entorno virtual ===
call .venv\Scripts\activate.bat

REM === Levantar Streamlit ===
python -m streamlit run analytics\streamlit_app.py

REM === Mantener la ventana abierta al final ===
pause
