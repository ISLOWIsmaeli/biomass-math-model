import tkinter as tk
from tkinter import ttk

class BiomassPowerPlantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biomass Power Plant Simulator")

        self.biomass_input_rate = tk.DoubleVar()
        self.power_output = tk.DoubleVar()
        self.steam_production_rate = tk.DoubleVar()

        canvas_frame = ttk.Frame(self.root)
        canvas_frame.pack()

        # Create canvas for flow diagram
        self.canvas = tk.Canvas(canvas_frame, width=600, height=400, bg="white")
        self.canvas.pack()

        # Draw flow diagram
        self.draw_flow_diagram()

        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Biomass Input Rate (kg/hour):").grid(row=0, column=0, sticky="w")
        self.input_entry = ttk.Entry(input_frame, textvariable=self.biomass_input_rate)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        self.calculate_button = ttk.Button(input_frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=1, columnspan=2, pady=10)

    def draw_flow_diagram(self):
        # Draw shapes
        self.canvas.create_rectangle(50, 50, 200, 100, outline="black", fill="lightblue")  # Boiler
        self.canvas.create_rectangle(250, 50, 400, 100, outline="black", fill="lightgreen")  # Turbine
        self.canvas.create_rectangle(450, 50, 600, 100, outline="black", fill="lightyellow")  # Generator

        # Draw arrows
        self.canvas.create_line(200, 75, 250, 75, arrow=tk.LAST)  # Arrow from boiler to turbine
        self.canvas.create_line(400, 75, 450, 75, arrow=tk.LAST)  # Arrow from turbine to generator

        # Draw labels
        self.canvas.create_text(125, 75, text="Biomass\nInput", anchor=tk.CENTER)
        self.canvas.create_text(325, 75, text="Steam", anchor=tk.CENTER)
        self.canvas.create_text(525, 75, text="Electricity", anchor=tk.CENTER)

        # Input box
        self.canvas.create_rectangle(50, 150, 200, 180, outline="black", fill="white")
        self.canvas.create_text(125, 165, text="Biomass\nInput Rate (kg/hour)", anchor=tk.CENTER)

        # Output box
        self.canvas.create_rectangle(450, 150, 600, 180, outline="black", fill="white")
        self.canvas.create_text(525, 165, text="Power Output (kW)\nSteam Production Rate (kg/hour)", anchor=tk.CENTER)

    def calculate(self):
        biomass_input_rate = self.biomass_input_rate.get()

        # Biomass properties (can be adjusted as needed)
        biomass_moisture_content = 0.1  # Example moisture content (%)
        biomass_lower_heating_value = 18000  # Example lower heating value (kJ/kg)

        # Boiler efficiency (can be adjusted as needed)
        boiler_efficiency = 0.80

        # Turbine efficiency (can be adjusted as needed)
        turbine_efficiency = 0.85

        # Generator efficiency (can be adjusted as needed)
        generator_efficiency = 0.90

        # Calculate the energy content of the biomass input
        biomass_energy_content = biomass_input_rate * (1 - biomass_moisture_content) * biomass_lower_heating_value

        # Calculate the steam production rate
        steam_production_rate = biomass_energy_content / (2260 * 100)  # Assuming enthalpy of vaporization of water is 2260 kJ/kg

        # Calculate the power output of the turbine
        turbine_power_output = steam_production_rate * turbine_efficiency

        # Calculate the electricity generated by the generator
        electricity_generated = turbine_power_output * generator_efficiency

        # Update the output box with the calculated values
        output_text = f"Power Output: {round(electricity_generated, 2)} kW\nSteam Production Rate: {round(steam_production_rate, 2)} kg/hour"
        self.canvas.create_text(525, 165, text=output_text, anchor=tk.CENTER)

def main():
    root = tk.Tk()
    app = BiomassPowerPlantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()