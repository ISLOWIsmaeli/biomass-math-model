# Define constants (assuming constant values)
Cp_w = 4.18  # kJ/kg⋅K (Specific heat capacity of water)
h_fg = 2257  # kJ/kg (Latent heat of vaporization of water)

def calculate_electrical_power():
  """
  This function prompts the user for input parameters and calculates the electrical power output of a biomass power plant.
  """
  # Get user input
  try:
    biomass_feed_rate = float(input("Enter biomass feed rate (tons/hour): "))
    lhv_b = float(input("Enter Lower Heating Value of biomass (MJ/kg): "))
    combustion_efficiency = float(input("Enter combustion efficiency (0-1): "))
    boiler_efficiency = float(input("Enter boiler efficiency (0-1): "))
    steam_turbine_efficiency = float(input("Enter steam turbine efficiency (0-1): "))
    generator_efficiency = float(input("Enter generator efficiency (0-1): "))
    feedwater_temp = float(input("Enter feedwater inlet temperature (°C): "))
    boiler_pressure_temp = float(input("Enter saturation temperature of steam at boiler pressure (°C): "))
  except ValueError:
    print("Invalid input. Please enter numerical values.")
    return

  # Convert biomass feed rate to kg/s
  biomass_feed_rate_kg_s = biomass_feed_rate * (1000 / 3600)  # tons/hour to kg/s

  # Calculate heat input rate
  heat_input_rate = biomass_feed_rate_kg_s * lhv_b * combustion_efficiency

  # Calculate steam mass flow rate
  steam_mass_flow_rate = heat_input_rate / ((Cp_w * (boiler_pressure_temp - feedwater_temp)) + h_fg) * boiler_efficiency

  # Calculate electrical power output
  electrical_power_output = steam_mass_flow_rate * h_fg * steam_turbine_efficiency * generator_efficiency

  # Print the results
  print("\nElectrical Power Output:", electrical_power_output, "MW")

if __name__ == "__main__":
  calculate_electrical_power()
