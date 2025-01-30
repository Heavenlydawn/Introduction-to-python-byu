# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500  # m/s²
WATER_DENSITY = 998.2000000  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa.s
PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters (11.294 inches)
PVC_SCHED80_FRICTION_FACTOR = 0.013  
SUPPLY_VELOCITY = 1.65 
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters (1.917 inches)
HDPE_SDR11_FRICTION_FACTOR = 0.018  
HOUSEHOLD_VELOCITY = 1.75  

def water_column_height(tower_height, tank_height):
    """Calculate and return the height of the water column."""
    h = tower_height + (3 * tank_height) / 4
    return h

def pressure_gain_from_water_height(height):
    """
    Calculate and return the pressure caused by Earth's gravity on the water.
    """
    P = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate and return the water pressure lost due to friction in the pipe.
    """
    P = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
    return P

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the pressure loss from pipe fittings like 45° and 90° bends.
    """
    P = (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000  
    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate the Reynolds number for the pipe with water flowing through it.
    """
    R = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the pressure loss due to a pipe reduction.
    """
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    P = (-k * WATER_DENSITY * fluid_velocity**2) / 2000 
    return P

def kPa_to_psi(kPa):
    """
    Convert pressure from kilopascals to pounds per square inch (psi).
    """
    return round(kPa * 0.145038, 4)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    
    pressure_in_psi = kPa_to_psi(pressure)
    
    print(f"Pressure at house: {pressure:.1f} kilopascals / {pressure_in_psi:.1f} psi")
    
if __name__ == "__main__":
    main()
