"""
Mini-Program 6: Game Character Creation System
Topic: Conditionals

Learning Objectives:
- Master complex nested conditional logic
- Use multiple logical operators in combination
- Implement state-dependent behavior
- Create a multi-step decision system
- Apply conditional logic to game mechanics

Instructions:
Complete this advanced character creation system for a role-playing game.
This is the most challenging conditionals program!
"""

# TODO 1: Create character base attributes
# character_name = "Hero"
# character_class = "Warrior"  # Options: Warrior, Mage, Rogue, Cleric
# level = 5
# health = 100
# mana = 50
# strength = 10
# intelligence = 8
# agility = 7
# Write your code here:


# TODO 2: Create character state variables
# is_alive = True
# is_poisoned = False
# is_buffed = False
# has_magic_item = True
# Write your code here:


# TODO 3: Apply class-based attribute modifiers
# If character_class == "Warrior":
#     strength += 5, health += 20
# elif character_class == "Mage":
#     intelligence += 5, mana += 30
# elif character_class == "Rogue":
#     agility += 5, health += 10
# elif character_class == "Cleric":
#     intelligence += 3, mana += 20, health += 15
# else:
#     Print "Invalid class"
# Write your code here:


# TODO 4: Calculate combat power based on class
# For Warrior: combat_power = strength * 2 + agility
# For Mage: combat_power = intelligence * 2 + (mana / 10)
# For Rogue: combat_power = agility * 2 + strength
# For Cleric: combat_power = (intelligence + strength) * 1.5
# Write your code here:


# TODO 5: Apply level-based bonuses
# For every level above 1, add 5 to health and 3 to mana
# Calculate bonus_health and bonus_mana based on (level - 1)
# Add these bonuses to current health and mana
# Write your code here:


# TODO 6: Check if character can use special abilities
# Create variable 'can_use_special'
# Warrior: level >= 3 and health > 50
# Mage: level >= 3 and mana > 40
# Rogue: level >= 3 and agility > 10
# Cleric: level >= 3 and (health > 50 or mana > 30)
# Write your code here:


# TODO 7: Apply status effects
# If is_poisoned is True:
#     Reduce health by 20
#     Print "Character is poisoned! Health reduced."
# Write your code here:


# TODO 8: Apply buff effects
# If is_buffed is True:
#     Increase combat_power by 25%
#     Print "Character is buffed! Combat power increased."
# Write your code here:


# TODO 9: Apply magic item effects
# If has_magic_item is True:
#     If character_class == "Mage" or character_class == "Cleric":
#         Increase intelligence by 3 and mana by 10
#     elif character_class == "Warrior":
#         Increase strength by 3 and health by 15
#     elif character_class == "Rogue":
#         Increase agility by 3
#     Print "Magic item equipped!"
# Write your code here:


# TODO 10: Check survival status
# If health <= 0:
#     is_alive = False
#     Print "Character has been defeated!"
# else:
#     Print "Character is alive and ready for battle!"
# Write your code here:


# TODO 11: Determine battle readiness level
# Create variable 'readiness'
# If combat_power > 50 and health > 75 and is_alive:
#     readiness = "Excellent"
# elif combat_power > 35 and health > 50 and is_alive:
#     readiness = "Good"
# elif combat_power > 20 and health > 25 and is_alive:
#     readiness = "Fair"
# elif is_alive:
#     readiness = "Poor"
# else:
#     readiness = "Defeated"
# Write your code here:


# TODO 12: Calculate equipment requirements for next upgrade
# Based on level, determine what equipment the character can use
# level < 5: equipment_tier = "Basic"
# level >= 5 and level < 10: equipment_tier = "Intermediate"
# level >= 10 and level < 15: equipment_tier = "Advanced"
# level >= 15: equipment_tier = "Legendary"
# Write your code here:


# TODO 13: Check if character can enter dungeon
# Create variable 'can_enter_dungeon'
# Requirements: is_alive and level >= 3 and combat_power >= 25
# If can_enter_dungeon:
#     Print "Ready to enter dungeon!"
# else:
#     Print "Not ready for dungeon. Improve your character."
# Write your code here:


# TODO 14: Implement a skill tree check
# Skills unlock based on level and class
# For Warrior (level >= 5): Print "Unlocked: Berserker Rage"
# For Mage (level >= 5 and intelligence >= 10): Print "Unlocked: Fireball Mastery"
# For Rogue (level >= 5 and agility >= 12): Print "Unlocked: Shadow Strike"
# For Cleric (level >= 5 and mana >= 50): Print "Unlocked: Divine Healing"
# Write your code here:


# TODO 15: Create a multi-condition quest eligibility check
# Create quest variables:
# quest_level_requirement = 4
# quest_requires_magic = True
# quest_requires_high_health = True
# Check if character meets ALL requirements:
# - level >= quest_level_requirement
# - If quest_requires_magic: (character_class == "Mage" or character_class == "Cleric") and mana > 30
# - If quest_requires_high_health: health > 60
# Print whether character is eligible for the quest
# Write your code here:


# TODO 16: Print complete character sheet
# Print all character information in a formatted way:
# - Name, Class, Level
# - Health, Mana
# - Strength, Intelligence, Agility
# - Combat Power
# - Status (Alive/Poisoned/Buffed)
# - Readiness Level
# - Equipment Tier
# Write your code here:


# BONUS TODO: Create a combat simulation
# Simulate a battle against an enemy with 40 health
# Character attacks based on combat_power (reduce enemy health)
# Enemy attacks back (reduce character health by 15)
# Use conditionals to determine who wins
# Account for special abilities, buffs, and status effects
# Print play-by-play commentary
# Write your code here:

