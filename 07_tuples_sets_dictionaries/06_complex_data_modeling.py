"""
Mini-Program 6: Complex Data Modeling and Analysis
Topic: Tuples, Sets and Dictionaries

Learning Objectives:
- Model complex real-world data using Python data structures
- Perform advanced data analysis operations
- Combine multiple data structures effectively
- Implement efficient data querying and filtering
- Solve complex problems with appropriate data structures

Instructions:
Complete this advanced data modeling program. This is the most
challenging tuples/sets/dictionaries program!
"""

# TODO 1: Create a social network graph
# users = {
#     'Alice': {'age': 25, 'city': 'NYC', 'friends': {'Bob', 'Charlie'}},
#     'Bob': {'age': 30, 'city': 'LA', 'friends': {'Alice', 'David'}},
#     'Charlie': {'age': 28, 'city': 'NYC', 'friends': {'Alice'}},
#     'David': {'age': 35, 'city': 'LA', 'friends': {'Bob'}}
# }
# Find:
# - Mutual friends between two users
# - Friend recommendations (friends of friends)
# - Users in same city with common friends
# Write your code here:


# TODO 2: Implement an inventory management system
# inventory = {
#     'A001': {'name': 'Laptop', 'quantity': 15, 'price': 999.99, 'category': 'Electronics'},
#     'A002': {'name': 'Mouse', 'quantity': 50, 'price': 29.99, 'category': 'Electronics'},
#     'B001': {'name': 'Desk', 'quantity': 8, 'price': 299.99, 'category': 'Furniture'}
# }
# Implement operations:
# - Find low stock items (quantity < threshold)
# - Calculate total inventory value
# - Group items by category
# - Find most expensive items
# - Search by name (partial match)
# Write your code here:


# TODO 3: Create a course enrollment system
# courses = {
#     'CS101': {'name': 'Intro to CS', 'capacity': 30, 'enrolled': {'Alice', 'Bob'}},
#     'CS102': {'name': 'Data Structures', 'capacity': 25, 'enrolled': {'Bob', 'Charlie'}},
#     'MATH201': {'name': 'Calculus', 'capacity': 40, 'enrolled': {'Alice', 'David'}}
# }
# students = {
#     'Alice': {'courses': {'CS101', 'MATH201'}, 'major': 'CS'},
#     'Bob': {'courses': {'CS101', 'CS102'}, 'major': 'CS'},
#     'Charlie': {'courses': {'CS102'}, 'major': 'Math'},
#     'David': {'courses': {'MATH201'}, 'major': 'Math'}
# }
# Implement:
# - Enroll student in course (check capacity)
# - Drop course
# - Find students with conflicting schedules
# - Recommend courses based on major
# - Find most popular courses
# Write your code here:


# TODO 4: Build a tournament bracket system
# players = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry')
# Create bracket structure using nested tuples/dictionaries
# Track match results: {('Alice', 'Bob'): 'Alice', ('Charlie', 'David'): 'David'}
# Advance winners to next round
# Determine tournament winner
# Write your code here:


# TODO 5: Implement a movie recommendation system
# movies = {
#     'Movie1': {'genres': {'Action', 'Sci-Fi'}, 'rating': 8.5, 'year': 2020},
#     'Movie2': {'genres': {'Drama', 'Romance'}, 'rating': 7.5, 'year': 2019},
#     'Movie3': {'genres': {'Action', 'Comedy'}, 'rating': 6.5, 'year': 2021}
# }
# user_preferences = {
#     'Alice': {'liked_genres': {'Action', 'Sci-Fi'}, 'min_rating': 7.0},
#     'Bob': {'liked_genres': {'Drama'}, 'min_rating': 8.0}
# }
# Recommend movies based on:
# - Genre match
# - Rating threshold
# - Recency (newer movies preferred)
# Calculate recommendation score
# Write your code here:


# TODO 6: Create a flight booking system
# flights = {
#     'FL001': {
#         'route': ('NYC', 'LA'),
#         'capacity': 200,
#         'booked': 150,
#         'price': 350,
#         'departure': '08:00'
#     },
#     'FL002': {
#         'route': ('LA', 'NYC'),
#         'capacity': 200,
#         'booked': 180,
#         'price': 320,
#         'departure': '14:00'
#     }
# }
# Implement:
# - Search flights by route
# - Check availability
# - Book seats (update booked count)
# - Find cheapest route
# - Calculate occupancy rate
# Write your code here:


# TODO 7: Build a restaurant order management system
# menu = {
#     'item1': {'name': 'Burger', 'price': 10.99, 'category': 'Main', 'available': True},
#     'item2': {'name': 'Fries', 'price': 3.99, 'category': 'Side', 'available': True},
#     'item3': {'name': 'Soda', 'price': 2.99, 'category': 'Drink', 'available': True}
# }
# orders = {
#     'order1': {
#         'items': {'item1': 2, 'item2': 1},  # item_id: quantity
#         'status': 'pending',
#         'table': 5
#     }
# }
# Implement:
# - Create new order
# - Calculate order total
# - Update order status
# - Find orders by table
# - Generate bill with tax
# Write your code here:


# TODO 8: Implement a library catalog system
# catalog = {
#     'book1': {
#         'title': 'Python Basics',
#         'authors': ('John Doe', 'Jane Smith'),
#         'isbn': '123-456',
#         'copies': 3,
#         'borrowed': {'Alice', 'Bob'}
#     }
# }
# Implement:
# - Search by title, author, or ISBN
# - Check availability
# - Borrow book (track who borrowed)
# - Return book
# - Find overdue books (add due dates)
# - Recommend books by same author
# Write your code here:


# TODO 9: Create a task dependency tracker
# tasks = {
#     'task1': {'name': 'Design', 'duration': 5, 'depends_on': set()},
#     'task2': {'name': 'Development', 'duration': 10, 'depends_on': {'task1'}},
#     'task3': {'name': 'Testing', 'duration': 7, 'depends_on': {'task2'}},
#     'task4': {'name': 'Documentation', 'duration': 3, 'depends_on': {'task1'}},
#     'task5': {'name': 'Deployment', 'duration': 2, 'depends_on': {'task3', 'task4'}}
# }
# Implement:
# - Find tasks that can start immediately
# - Calculate earliest start time for each task
# - Find critical path (longest path to completion)
# - Detect circular dependencies
# - Find all tasks that must complete before a given task
# Write your code here:


# TODO 10: Build a voting system analyzer
# votes = {
#     'voter1': {'candidate': 'Alice', 'district': 'D1', 'timestamp': '2024-01-01 10:00'},
#     'voter2': {'candidate': 'Bob', 'district': 'D1', 'timestamp': '2024-01-01 10:05'},
#     'voter3': {'candidate': 'Alice', 'district': 'D2', 'timestamp': '2024-01-01 10:10'}
# }
# Analyze:
# - Total votes per candidate
# - Votes by district
# - Winner overall and per district
# - Voting patterns over time
# - Detect duplicate votes (same voter ID)
# Write your code here:


# BONUS TODO: Implement a complete e-commerce system
# Combine all concepts to create an e-commerce platform with:
# - Products (with categories, prices, inventory)
# - Users (with cart, wishlist, order history)
# - Orders (with items, status, shipping info)
# - Reviews (with ratings, comments)
# Implement operations:
# - Add to cart
# - Place order (check inventory, calculate total)
# - Track order status
# - Product recommendations based on purchase history
# - Calculate store statistics (revenue, popular products, etc.)
# This is very comprehensive!
# Write your code here:

