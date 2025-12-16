"""
Mini-Program 6: Complete OOP Application - Game System
Topic: Basic OOP

Learning Objectives:
- Design a complete application using OOP principles
- Create multiple interacting classes
- Manage complex object relationships
- Implement game logic with objects
- Apply all basic OOP concepts together

Instructions:
Complete this comprehensive game system. This is the most challenging
basic OOP program!
"""

# TODO 1: Create an Item class
# Attributes: name, item_type (weapon/armor/potion), value, description
# Methods: use(), get_info()
# Write your code here:


# TODO 2: Create an Inventory class
# Attributes: items (list of Item objects), max_capacity
# Methods:
# - add_item(item) - check capacity
# - remove_item(item_name)
# - find_item(item_name)
# - list_items()
# - get_total_value()
# - is_full()
# Write your code here:


# TODO 3: Create a Stats class
# Attributes: health, max_health, attack, defense, speed
# Methods:
# - take_damage(amount)
# - heal(amount)
# - is_alive()
# - get_stats()
# Write your code here:


# TODO 4: Create a Character class (base for player and enemies)
# Attributes: name, level, stats (Stats object), inventory (Inventory object)
# Methods:
# - attack_target(target)
# - use_item(item_name)
# - level_up()
# - is_alive()
# - get_character_info()
# Write your code here:


# TODO 5: Create a Player class (inherits from Character)
# Additional attributes: experience, gold
# Additional methods:
# - gain_experience(amount)
# - add_gold(amount)
# - spend_gold(amount)
# - get_player_info()
# Write your code here:


# TODO 6: Create an Enemy class (inherits from Character)
# Additional attributes: enemy_type, reward_exp, reward_gold
# Additional methods:
# - get_enemy_info()
# - get_rewards() - returns tuple (exp, gold)
# Write your code here:


# TODO 7: Create a Location class
# Attributes: name, description, enemies (list), items (list), connected_locations (dict)
# Methods:
# - add_enemy(enemy)
# - remove_enemy(enemy)
# - add_item(item)
# - remove_item(item)
# - connect_location(direction, location)
# - get_available_directions()
# - get_location_info()
# Write your code here:


# TODO 8: Create a Battle class
# Manages combat between player and enemy
# Methods:
# - start_battle(player, enemy)
# - player_turn(action) - actions: attack, use_item, flee
# - enemy_turn()
# - is_battle_over()
# - get_winner()
# Write your code here:


# TODO 9: Create a Quest class
# Attributes: quest_id, name, description, objective, reward_exp, reward_gold, completed
# Methods:
# - complete_quest()
# - get_quest_info()
# - is_completed()
# Write your code here:


# TODO 10: Create a QuestLog class
# Attributes: active_quests (list), completed_quests (list)
# Methods:
# - add_quest(quest)
# - complete_quest(quest_id)
# - list_active_quests()
# - list_completed_quests()
# - get_total_quests_completed()
# Write your code here:


# TODO 11: Create a Shop class
# Attributes: shop_name, items_for_sale (list of items with prices)
# Methods:
# - add_item_to_shop(item, price)
# - buy_item(player, item_name)
# - sell_item(player, item_name)
# - list_items()
# Write your code here:


# TODO 12: Create a Game class (main game controller)
# Attributes: player, current_location, locations (dict), quest_log
# Methods:
# - start_game()
# - move_player(direction)
# - explore_location()
# - initiate_battle(enemy)
# - visit_shop()
# - display_player_status()
# - save_game()
# - load_game()
# Write your code here:


# TODO 13: Initialize the game world
# Create several locations
# Connect locations to each other
# Place enemies in locations
# Place items in locations
# Create quests
# Write your code here:


# TODO 14: Create the player character
# Initialize player with starting stats
# Give starting equipment
# Add starting gold
# Write your code here:


# TODO 15: Implement game loop
# Main game loop that:
# - Displays current location
# - Shows available actions
# - Processes player input
# - Updates game state
# - Checks win/loss conditions
# Actions: move, fight, search, inventory, status, quit
# Write your code here:


# TODO 16: Implement combat system
# When player encounters enemy:
# - Display enemy info
# - Enter battle mode
# - Allow actions: attack, use potion, flee
# - Process turns
# - Handle victory (gain exp, gold, items)
# - Handle defeat (game over)
# Write your code here:


# TODO 17: Implement progression system
# - Track experience points
# - Level up when threshold reached
# - Increase stats on level up
# - Display level up message
# Write your code here:


# TODO 18: Create sample gameplay scenario
# Player starts in "Village"
# Can explore "Forest" (has weak enemies)
# Can visit "Shop" to buy items
# Can enter "Cave" (has stronger enemies)
# Quest: Defeat 3 enemies in forest
# Implement and test this scenario
# Write your code here:


# TODO 19: Add game statistics tracking
# Create GameStats class that tracks:
# - Total enemies defeated
# - Total gold earned
# - Total items collected
# - Locations visited
# - Time played (simulated turns)
# Display stats at game end
# Write your code here:


# BONUS TODO: Implement save/load system
# Save game state to a file:
# - Player stats and inventory
# - Current location
# - Quest progress
# - World state
# Load game state from file
# Allow continuing from saved game
# Handle save file corruption
# This is very comprehensive!
# Write your code here:

