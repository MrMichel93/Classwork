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
# Constants
# TODO 1-6: Model the free-fall scenario
# Create the gravity and free-fall variables, then calculate and print the falling object's final velocity and distance.
# Hint: final_velocity = initial_velocity + (gravity * time_falling)
# Hint: distance_fallen = initial_velocity * time_falling + 0.5 * gravity * time_falling ** 2
# Write your code here:


# SCENARIO 2: Projectile Launch
# TODO 7-11: Model the projectile launch
# Create the launch variables, find the maximum height and time values, and print the launch summary.
# Hint: max_height = (v ** 2 - u ** 2) / (2 * a), time_to_max = (v - u) / a, total_air_time = time_to_max * 2
# Write your code here:


# SCENARIO 3: Energy Calculations
# TODO 12-16: Calculate the car's energy values
# Create the mass, velocity, and hill variables, then calculate kinetic, potential, and total mechanical energy.
# Print the energy summary with labels.
# Hint: car_kinetic_energy = 0.5 * car_mass * car_velocity ** 2
# Hint: car_potential_energy = car_mass * gravity * hill_height, total_energy = car_kinetic_energy + car_potential_energy
# Write your code here:


# SCENARIO 4: Braking Distance
# TODO 17-21: Analyze the braking phase
# Create the braking variables, calculate the stopping distance, stopping time, and work done by the brakes, then print the results.
# Hint: braking_distance = (v ** 2 - u ** 2) / (2 * deceleration), braking_time = (v - u) / deceleration
# Hint: work_by_brakes = car_kinetic_energy - 0
# Write your code here:


# BONUS TODO: Extend the simulator with a rocket trip
# Build a two-phase motion example for the rocket and report its velocity, distances, total distance, and average velocity.
# Write your code here:
