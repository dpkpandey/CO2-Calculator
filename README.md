# CO2-Calculator

IF you work in aquaculture or you have aquirium and you want to measure CO2 and its relation with Alkalinity, pH, temperature, Salinity
then this is explanation repo for this calculator you can visualize through "[streamlitCO2](https://co2calculator.streamlit.app/)"
Just visit there and Enjoy the calculator.


## If you want to run locally in your computer
Well we have easy way to do.
Install python and
clone this repo
```bash
git clone https://github.com/dpkpandey/CO2-Calculator
cd Co2-Calculator
pip install -r requirements.txt
```
if you have a problem installing requirements.txt file then it is better to remove version 
and create virtual environment for easy ness as this 
```bash
git clone https://github.com/dpkpandey/CO2-Calculator
cd Co2-Calculator
python -m venv myenv
source myeve/Scripts/activate  # for Windows
source myenve\bin\activate  # for Linux
pip install -r requirements.txt
```

if you have a problem with name Co2-Calculator while running code just change it to Co2_Calculator for smoothness

then run 
```bash
streamlit run co2.streamlit.py
```

Enjoy 
