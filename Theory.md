# Theoretical Concepts in CO₂ Calculation and Visualization

## Introduction
This document outlines the theoretical concepts behind the CO₂ calculation and visualization tool implemented using Streamlit and Matplotlib. The application calculates the concentration of carbon dioxide (CO₂) in water based on input parameters such as alkalinity, salinity, temperature, and pH. The CO₂ levels are then categorized into safe, cautionary, or severe conditions and visualized through graphs.

## CO₂ Calculation
The formula used to compute CO₂ concentration is:

\[ CO_2 = 1.22 \times (Alkalinity) \times 10^{(-43.6977 - 0.0129037 \times (Salinity) + 1.364 \times 10^{-4} \times (Salinity)^2 + 2885.378 / (273.15 + Temp) + 7.045159 \times \log(273.15 + Temp)) - pH} \]

### Parameters:
- **Alkalinity (mg/L):** The capacity of water to neutralize acids, measured in milligrams per liter (mg/L).
- **Salinity (ppt):** The concentration of dissolved salts in water, expressed in parts per thousand (ppt).
- **Temperature (°C):** The water temperature in degrees Celsius.
- **pH:** A measure of the acidity or alkalinity of the water on a scale from 0 to 14.

### Interpretation of CO₂ Levels:
- **CO₂ < 20:** Safe
- **20 ≤ CO₂ ≤ 30:** Caution
- **CO₂ > 30:** Severe

These categories help users assess the water quality and take necessary actions.

## Data Visualization
To aid in understanding how CO₂ levels vary with different parameters, two graphical representations are provided:

### Graph 1: CO₂ vs Various Variables
This graph visualizes the relationship between CO₂ levels and individual water parameters:
- CO₂ vs Salinity
- CO₂ vs Temperature
- CO₂ vs Alkalinity
- CO₂ vs pH

Each variable is plotted while keeping other parameters constant, allowing for comparative analysis.

### Graph 2: Multi-Panel Comparison
This visualization splits the CO₂ data into four separate subplots, showing:
1. CO₂ vs Salinity
2. CO₂ vs Temperature
3. CO₂ vs Alkalinity
4. CO₂ vs pH

Each subplot highlights the effect of a specific variable while keeping the others constant, making it easier to identify trends.

## Application Implementation
The tool is built using **Streamlit**, a Python library for creating interactive web applications. Users can input values for alkalinity, salinity, temperature, and pH, and the system will compute CO₂ levels dynamically.

### Features:
- **Numeric Input Fields:** Allows users to enter values for the key parameters.
- **CO₂ Calculation:** Uses the predefined formula to compute CO₂.
- **Graph Selection:** Users can choose between two visualization types.
- **Results Interpretation:** Displays CO₂ level with safety categorization.

## Conclusion
This CO₂ calculation and visualization tool provides an interactive way to analyze the impact of various parameters on CO₂ concentration in water. The combination of numerical computation and graphical representation enhances understanding and decision-making in aquatic environments.

