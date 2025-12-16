"""
Mini-Program 6: Physics Motion Simulator
Topic: Variables, Expressions and Statements

Learning Objectives:
- Apply multiple complex physics formulas
- Chain calculations where one result feeds into another
- Work with scientific notation and large numbers
- Understand variable dependencies in multi-step problems
- Combine multiple mathematical operations

Instructions:
Complete this physics simulator that calculates various aspects of
projectile motion and energy. This is the most challenging program
in this topic!
"""

# Physics formulas used in this program:
# Distance: d = v * t (distance = velocity × time)
# Acceleration: v = u + at (final velocity = initial velocity + acceleration × time)
# Kinetic Energy: KE = 0.5 * m * v^2
# Potential Energy: PE = m * g * h
# Position under constant acceleration: s = ut + 0.5 * a * t^2

# Constants
# TODO 1: Create a variable 'gravity' and set it to 9.81 (m/s^2 on Earth)
# Write your code here:


# SCENARIO 1: Free Fall Object
# TODO 2: An object is dropped from a height. Initial velocity is 0 m/s
# Create variable 'initial_velocity' = 0.0
# Write your code here:


# TODO 3: Create a variable 'time_falling' and set it to 3.0 seconds
# Write your code here:


# TODO 4: Calculate the final velocity after falling
# Formula: final_velocity = initial_velocity + (gravity * time_falling)
# Write your code here:


# TODO 5: Calculate the distance fallen
# Formula: distance = initial_velocity * time_falling + 0.5 * gravity * time_falling^2
# Store in 'distance_fallen'
# Write your code here:


# TODO 6: Print the final velocity and distance fallen
# Write your code here:


# SCENARIO 2: Projectile Launch
# TODO 7: A ball is thrown upward with initial velocity of 20 m/s
# Create variable 'launch_velocity' = 20.0
# Write your code here:


# TODO 8: Calculate the maximum height reached
# At max height, final velocity = 0
# Use: v^2 = u^2 + 2as, rearranged to: s = (v^2 - u^2) / (2*a)
# Note: acceleration is negative (gravity pulls down), so use -gravity
# Store in 'max_height'
# Write your code here:


# TODO 9: Calculate the time to reach maximum height
# Use: t = (v - u) / a
# Store in 'time_to_max'
# Write your code here:


# TODO 10: Calculate the total time in the air (goes up and comes back down)
# Total time = time_to_max * 2
# Store in 'total_air_time'
# Write your code here:


# TODO 11: Print the maximum height and total air time
# Write your code here:


# SCENARIO 3: Energy Calculations
# TODO 12: A car with mass 1200 kg is traveling at 25 m/s
# Create variables: car_mass = 1200.0, car_velocity = 25.0
# Write your code here:


# TODO 13: Calculate the kinetic energy of the car
# Formula: kinetic_energy = 0.5 * mass * velocity^2
# Store in 'car_kinetic_energy'
# Write your code here:


# TODO 14: The car goes up a hill that is 50 meters high
# Calculate the potential energy at the top
# Formula: potential_energy = mass * gravity * height
# Create variable hill_height = 50.0
# Store PE in 'car_potential_energy'
# Write your code here:


# TODO 15: Calculate total mechanical energy (KE + PE) at the top of the hill
# Assuming no energy loss
# Store in 'total_energy'
# Write your code here:


# TODO 16: Print all energy values with labels
# Write your code here:


# SCENARIO 4: Braking Distance
# TODO 17: Calculate how far the car travels while braking to a stop
# Initial velocity: 25 m/s, Final velocity: 0 m/s
# Deceleration (negative acceleration): -5.0 m/s^2
# Use: s = (v^2 - u^2) / (2*a)
# Store in 'braking_distance'
# Create variable 'deceleration' = -5.0
# Write your code here:


# TODO 18: Calculate the braking time
# Use: t = (v - u) / a
# Store in 'braking_time'
# Write your code here:


# TODO 19: Print the braking distance and time
# Write your code here:


# TODO 20: Calculate work done by brakes (energy dissipated)
# Work = change in kinetic energy = initial KE - final KE
# Final KE is 0 (car stops)
# Store in 'work_by_brakes'
# Write your code here:


# TODO 21: Print the work done by brakes
# Write your code here:


# BONUS TODO: Complex Scenario
# A rocket starts from rest and accelerates at 15 m/s^2 for 10 seconds.
# Then it continues at constant velocity for another 20 seconds.
# Calculate:
# 1. Velocity after acceleration phase
# 2. Distance covered during acceleration
# 3. Distance covered at constant velocity
# 4. Total distance traveled
# 5. Average velocity for the entire journey
# Write your code here:

