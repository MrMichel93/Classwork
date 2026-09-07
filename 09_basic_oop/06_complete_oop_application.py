"""
Mini-Program 6: OOP Capstone - Game System
Topic: Basic OOP (University Enrichment)

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

# TODO 1-6: Create the core game entities
# Build Item with name, item_type, value, description plus use() and get_info()
# Build Inventory with item-management methods such as add_item(item), remove_item(item_name), find_item(item_name), list_items(), get_total_value(), and is_full()
# Build Stats with combat-related values and methods such as take_damage(amount), heal(amount), is_alive(), and get_stats()
# Build Character as a shared base, then extend it with Player and Enemy subclasses
# Give Player progression and currency behavior, and give Enemy type/reward behavior including get_rewards()
# Hint: class Character: def attack_target(self, target): ... / def use_item(self, item_name): ...
# Hint: class Player(Character): ...
# Hint: class Enemy(Character): def get_rewards(self): ...
# Write your code here:


# TODO 7-12: Create the world and gameplay systems
# Build Location to manage connected places, enemies, and items
# Build Battle to coordinate turn-based combat between a player and an enemy
# Build Quest and QuestLog to track objectives and completion
# Build Shop for buying and selling items
# Build Game as the main controller with methods such as start_game(), move_player(direction), explore_location(), initiate_battle(enemy), visit_shop(), display_player_status(), save_game(), and load_game()
# Hint: class Location: def connect_location(self, direction, location): ...
# Hint: class Battle: def player_turn(self, action): ...
# Hint: class Game: def start_game(self): ...
# Write your code here:


# TODO 13-19: Assemble a playable scenario and supporting systems
# Initialize a small world with connected locations, placed enemies, items, quests, and a starting player
# Build a main game loop that presents actions, updates state, and checks for win/loss conditions
# Add combat flow, experience-based progression, and a sample scenario featuring places like Village, Forest, Shop, and Cave
# Build GameStats to track progress such as enemies defeated, gold earned, items collected, visited locations, and simulated turns played
# Demonstrate the scenario so the interacting classes work together as one application
# Hint: class GameStats: ...
# Write your code here:


# BONUS TODO: Extend the game with a save/load system
# Persist and restore key state such as player progress, inventory, quests, current location, and world changes
# Include reasonable handling for missing or invalid save data
# Write your code here:
