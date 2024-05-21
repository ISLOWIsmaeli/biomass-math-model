import tkinter as tk
from tkinter import messagebox

# Define constants (assuming constant values)
Cp_w = 4.18  # kJ/kg⋅K (Specific heat capacity of water)
h_fg = 2257  # kJ/kg (Latent heat of vaporization of water)

def calculate_electrical_power():
    try:
        biomass_feed_rate = float(biomass_feed_rate_entry.get())
        lhv_b = float(lhv_b_entry.get())
        combustion_efficiency = float(combustion_efficiency_entry.get())
        boiler_efficiency = float(boiler_efficiency_entry.get())
        steam_turbine_efficiency = float(steam_turbine_efficiency_entry.get())
        generator_efficiency = float(generator_efficiency_entry.get())
        feedwater_temp = float(feedwater_temp_entry.get())
        boiler_pressure_temp = float(boiler_pressure_temp_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
        return

    # Convert biomass feed rate to kg/s
    biomass_feed_rate_kg_s = biomass_feed_rate * (1000 / 3600)  # tons/hour to kg/s

    # Calculate heat input rate
    heat_input_rate = biomass_feed_rate_kg_s * lhv_b * combustion_efficiency

    # Calculate steam mass flow rate
    steam_mass_flow_rate = heat_input_rate / ((Cp_w * (boiler_pressure_temp - feedwater_temp)) + h_fg) * boiler_efficiency

    # Calculate electrical power output
    electrical_power_output = steam_mass_flow_rate * h_fg * steam_turbine_efficiency * generator_efficiency

    # Display the results
    result_label.config(text=f"Electrical Power Output: {electrical_power_output:.2f} MW")

# Create the main window
root = tk.Tk()
root.title("Biomass Power Plant Simulation")

# Create and place input fields and labels
tk.Label(root, text="Biomass feed rate (tons/hour):").grid(row=0, column=0, sticky="e")
biomass_feed_rate_entry = tk.Entry(root)
biomass_feed_rate_entry.grid(row=0, column=1)

tk.Label(root, text="Lower Heating Value of biomass (MJ/kg):").grid(row=1, column=0, sticky="e")
lhv_b_entry = tk.Entry(root)
lhv_b_entry.grid(row=1, column=1)

tk.Label(root, text="Combustion efficiency (0-1):").grid(row=2, column=0, sticky="e")
combustion_efficiency_entry = tk.Entry(root)
combustion_efficiency_entry.grid(row=2, column=1)

tk.Label(root, text="Boiler efficiency (0-1):").grid(row=3, column=0, sticky="e")
boiler_efficiency_entry = tk.Entry(root)
boiler_efficiency_entry.grid(row=3, column=1)

tk.Label(root, text="Steam turbine efficiency (0-1):").grid(row=4, column=0, sticky="e")
steam_turbine_efficiency_entry = tk.Entry(root)
steam_turbine_efficiency_entry.grid(row=4, column=1)

tk.Label(root, text="Generator efficiency (0-1):").grid(row=5, column=0, sticky="e")
generator_efficiency_entry = tk.Entry(root)
generator_efficiency_entry.grid(row=5, column=1)

tk.Label(root, text="Feedwater inlet temperature (°C):").grid(row=6, column=0, sticky="e")
feedwater_temp_entry = tk.Entry(root)
feedwater_temp_entry.grid(row=6, column=1)

tk.Label(root, text="Saturation temperature of steam at boiler pressure (°C):").grid(row=7, column=0, sticky="e")
boiler_pressure_temp_entry = tk.Entry(root)
boiler_pressure_temp_entry.grid(row=7, column=1)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_electrical_power)
calculate_button.grid(row=8, column=0, columnspan=2)

# Create and place the result label
result_label = tk.Label(root, text="Electrical Power Output: ")
result_label.grid(row=9, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
