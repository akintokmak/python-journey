# Day 16: Coffee Machine - Object Oriented Programming (OOP) ☕

In this project, I transitioned from procedural programming to **Object-Oriented Programming (OOP)**. I used pre-defined classes to handle the machine's resources, menu, and payment system, focusing my development on the **main logic integration**.

## 🏗️ The Power of OOP
The most striking part of this project is how much the code was simplified compared to Day 15. By utilizing objects and methods, I managed the entire machine logic in just a few lines of code in `main.py`.

## 🛠️ Classes Used
- `MenuItem`: Models each drink on the menu.
- `Menu`: Manages the available drinks and handles user selection.
- `CoffeeMaker`: Handles the machine's resources (Water, Milk, Coffee) and brewing process.
- `MoneyMachine`: Manages the coin-operated payment system and transactions.

## 💻 My Contribution: main.py
I developed the core execution logic in `main.py`, which:
- Initializes the machine objects.
- Handles the main operational loop (order -> payment -> brew).
- Manages administrative commands like `off` and `report`.

## 📂 Project Structure
- `main.py`: **(Written by me)** Orchestrates the entire system logic.
- `menu.py`: Contains `MenuItem` and `Menu` classes.
- `coffee_maker.py`: Contains the `CoffeeMaker` class.
- `money_machine.py`: Contains the `MoneyMachine` class.