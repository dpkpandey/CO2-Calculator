import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def expression(Alkalinity, Salinity, Temp, pH):
    return 1.22 * (Alkalinity) * 10 ** (
        (-43.6977 - 0.0129037 * (Salinity) + 1.364 * 10 ** (-4) * (Salinity) ** 2 + 2885.378 / (273.15 + Temp)
         + 7.045159 * np.log(273.15 + Temp)) - pH)

def calculate_CO2(Alkalinity, Salinity, Temp, pH):
    try:
        CO2 = expression(Alkalinity, Salinity, Temp, pH)

        st.write(f"CO2: {CO2:.4f}")
        if CO2 < 20:
            st.write(f"CO2: {CO2:.4f} (Safe)")
        elif 20 <= CO2 <= 30:
            st.write(f"CO2: {CO2:.4f} (Caution)")
        else:
            st.write(f"CO2: {CO2:.4f} (Severe)")

        # Plot the selected graph with user-entered values
        if graph_type == 1:
            plot_graph1(Alkalinity, Salinity, Temp, pH)
        elif graph_type == 2:
            plot_graph2(Alkalinity, Salinity, Temp, pH)

    except ValueError:
        st.error("Error!!! Barramundi is not happy. Please enter valid numeric values.")

# Generate sample data
Alkalinity_values = np.arange(0.00, 1000, 4)
Salinity_values = np.arange(0, 80, 0.2)
Temp_values = np.arange(0, 100, 0.2)
pH_values = np.arange(0, 14, 0.045)

def plot_graph1(Alkalinity, Salinity, Temp, pH):
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(Salinity_values, expression(Alkalinity, Salinity_values, Temp, pH),
            label=f'Salinity -(At const Alkalinity, Alkalinity={Alkalinity},  TEMP={Temp}, pH={pH})', color='blue')

    # Plot for CO2 vs Temperature
    ax.plot(Temp_values, expression(Alkalinity, Salinity, Temp_values, pH),
            label=f"Temperature -(At const Alkalinity, Alkalinity={Alkalinity}, Salinity={Salinity}, pH={pH})",
            color='green')

    # Plot for cO2 vs Alkalinity
    ax.plot(Alkalinity_values, expression(Alkalinity_values, Salinity, Temp, pH),
            label=f"Alkalinity -(At const Alkalinity, pH={pH}, Salinity={Salinity}, TEMP={Temp})", color='purple')

    # Plot for CO2 vs pH
    ax.plot(pH_values, expression(Alkalinity, Salinity, Temp, pH_values),
            label=f"pH - (At const Alkalinity, Alkalinity={Alkalinity}, Salinity={Salinity}, TEMP={Temp})", color='red')

    # Add a big circle for the value of Toxic Ammonia
    CO2 = expression(Alkalinity, Salinity, Temp, pH)
    ax.plot(pH, CO2, 'ro', markersize=10)
    ax.plot(Temp, CO2, 'go', markersize=10)
    ax.plot(Salinity, CO2, 'bo', markersize=10)
    ax.plot(Alkalinity, CO2, 'o', color='purple', markersize=10)

    # Set labels and title
    ax.set_xlabel('Variables')
    ax.set_ylabel('CO2')
    ax.set_title('CO2 vs Various Variables')
    ax.legend(loc='upper right')
    plt.xlim(0, 30)
    plt.grid(True)
    plt.xticks(rotation=90)
    plt.xticks(np.arange(0, 400, 5))
    plt.ylim(0, CO2 * 2)
    plt.yticks(np.arange(0, CO2 * 2, CO2 / 3))

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    st.pyplot(fig)

def plot_graph2(Alkalinity, Salinity, Temp, pH):
    fig, axs = plt.subplots(2, 2, figsize=(14, 5))
    plt.tight_layout()
    CO2 = expression(Alkalinity, Salinity, Temp, pH)

    axs[0, 0].plot(Salinity_values, expression(Alkalinity, Salinity_values, Temp, pH),
                   label=f'Alkalinity={Alkalinity},  TEMP={Temp}, pH={pH} fixed')
    axs[0, 0].set_xlabel('Salinity')
    axs[0, 0].set_ylabel('CO2')
    axs[0, 0].set_title('CO2 vs Salinity')
    axs[0, 0].legend()

    axs[0, 1].plot(Temp_values, expression(Alkalinity, Salinity, Temp_values, pH),
                   label=f"Alkalinity={Alkalinity}, Salinity={Salinity}, pH={pH} fixed", color='green')
    axs[0, 1].set_xlabel('Temperature')
    axs[0, 1].set_ylabel('CO2')
    axs[0, 1].set_title('CO2 vs Temperature')
    axs[0, 1].legend()

    axs[1, 0].plot(Alkalinity_values, expression(Alkalinity_values, Salinity, Temp, pH),
                   label=f"pH={pH}, Salinity={Salinity}, TEMP={Temp} fixed", color='purple')
    axs[1, 0].set_xlabel('Alkalinity')
    axs[1, 0].set_ylabel('CO2')
    axs[1, 0].set_title('CO2 vs Alkalinity')
    axs[1, 0].legend()

    axs[1, 1].plot(pH_values, expression(Alkalinity, Salinity, Temp, pH_values),
                   label=f"Alkalinity={Alkalinity}, Salinity={Salinity}, TEMP={Temp} fixed", color='red')
    axs[1, 1].set_xlabel('pH')
    axs[1, 1].set_ylabel('CO2')
    axs[1, 1].set_title('CO2 vs pH')
    axs[1, 1].legend()

    axs[0, 0].grid(True)
    axs[0, 1].grid(True)
    axs[1, 0].grid(True)
    axs[1, 1].grid(True)

    axs[0, 0].plot(Salinity, expression(Alkalinity, Salinity, Temp, pH), 'bo', markersize=10)
    axs[0, 1].plot(Temp, expression(Alkalinity, Salinity, Temp, pH), 'go', markersize=10)
    axs[1, 0].plot(Alkalinity, expression(Alkalinity, Salinity, Temp, pH), 'o', color='purple', markersize=10)
    axs[1, 1].plot(pH, expression(Alkalinity, Salinity, Temp, pH), 'ro', markersize=10)

    plt.tight_layout()

    # Show the plots
    st.pyplot(fig)

# Streamlit app starts here
st.title("CO2 Calculator")

Alkalinity = st.number_input("Alkalinity (mg/l):", min_value=0.0)
Salinity = st.number_input("Salinity (ppt):", min_value=0.0)
Temp = st.number_input("Temperature (Celsius):", min_value=0.0)
pH = st.number_input("pH:", min_value=0.0)

# Create radio buttons for graph type selection
graph_type = st.radio("Select Graph Type", options=[1, 2], index=0)

# Create the Calculate button
if st.button("Calculate"):
    calculate_CO2(Alkalinity, Salinity, Temp, pH)

# Create a button to clear entries
if st.button("Clear"):
    st.experimental_rerun()

# Display result label
result_label = st.empty()

# Initialize result_label with an empty string to avoid streamlit error
result_label.text("")

# You can add other controls or messages as needed
