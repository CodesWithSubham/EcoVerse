import sys

def calculate_carbon_footprint(electricity_kwh, vehicle_km):
    """
    Calculates the estimated carbon footprint based on standard emission factors.
    - Electricity: ~0.85 kg CO2 per kWh
    - Average Car: ~0.14 kg CO2 per km
    """
    # Fix: Reject negative inputs as requested by CodeRabbit
    if electricity_kwh < 0 or vehicle_km < 0:
        raise ValueError("Electricity usage and vehicle distance must be non-negative.")

    ELEC_EMISSION_FACTOR = 0.85
    CAR_EMISSION_FACTOR = 0.14

    electricity_emissions = electricity_kwh * ELEC_EMISSION_FACTOR
    transport_emissions = vehicle_km * CAR_EMISSION_FACTOR
    
    total_emissions = electricity_emissions + transport_emissions
    return total_emissions, electricity_emissions, transport_emissions

def main():
    print("🌱 EcoVerse Offline Carbon Calculator 🌱")
    print("-" * 40)
    
    try:
        elec = float(input("Enter monthly electricity usage (in kWh): "))
        trans = float(input("Enter monthly vehicle distance traveled (in km): "))
        
        total, e_emissions, t_emissions = calculate_carbon_footprint(elec, trans)
        
        print("\n📊 --- Carbon Footprint Report --- 📊")
        print(f"Electricity Emissions: {e_emissions:.2f} kg CO2")
        print(f"Transport Emissions:   {t_emissions:.2f} kg CO2")
        print(f"Total Carbon Footprint: {total:.2f} kg CO2")
        print("-" * 40)
        
    except ValueError as e:
        # Fix: Catch specific error and exit with a non-zero code
        if str(e).startswith("could not convert string to float"):
            print("❌ Error: Please enter valid numeric values.")
        else:
            print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()