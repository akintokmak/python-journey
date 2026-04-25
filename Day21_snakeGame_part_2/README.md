# Day 21: Snake Game - Part 2 (Inheritance & Game Logic) 🐍

This stage completes the fully functional Snake Game. The focus was on Object-Oriented Programming (OOP) principles, specifically **Inheritance**, and implementing game mechanics like collision detection and score tracking.

## 🚀 Features Implemented
- **Food Class (Inheritance):** Created a `Food` class that inherits from the `Turtle` class. It manages its own appearance and random relocation logic.
- **Scoreboard Class:** A dedicated class to handle real-time scoring and the "Game Over" sequence, also utilizing inheritance.
- **Collision Detection:** - Wall Collisions: Checks if the snake's head hits the screen boundaries.
  - Tail Collisions: Uses **Python Slicing** to check if the head collides with any body segment.
- **Dynamic Growth:** The snake grows longer every time it consumes food.

## 🏗️ Technical Highlight: Class Inheritance
Instead of creating a turtle and then configuring it inside the main file, I extended the `Turtle` class. This allows the `Food` object to *be* a turtle while having its own custom `refresh()` method.



## ✂️ Advanced Python: List Slicing
To efficiently check for tail collisions without checking the head itself, I used slicing:
```python
for segment in segments[1:]:
    if head.distance(segment) < 10:
        game_is_on = False