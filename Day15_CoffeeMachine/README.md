# Day 15: Digital Coffee Machine ☕

A robust command-line coffee machine simulation built with Python. This project focuses on **resource management**, **transaction logic**, and **input validation**.

## 🛠 Features
- **Menu Selection:** Choose between Espresso, Latte, and Cappuccino.
- **Resource Monitoring:** Tracks Water, Milk, and Coffee levels in real-time.
- **Coin Processing:** Accepts Quarters, Dimes, Nickels, and Pennies, calculating the total and providing change.
- **Safety Checks:** - Verifies if there are enough ingredients before starting an order.
    - Validates if the inserted money is sufficient for the chosen drink.
- **Admin Commands:** - `Report`: View current resource levels and total profit.
    - `Off`: Safely shut down the machine for maintenance.

## 🧠 Technical Highlights
- **Error Handling:** Implemented `try-except` blocks to handle invalid numeric inputs during coin insertion, preventing program crashes.
- **Data Encapsulation:** Used nested dictionaries to manage menu prices and ingredient requirements dynamically.
- **Modular Logic:** Divided the program into clear, functional blocks such as `check_resources`, `process_coins`, and `make_coffee` for better maintainability.

## 🚀 How to Run
1. Run `coffee_machine.py`.
2. Type your drink choice when prompted.
3. Insert coins as requested.
4. Enjoy your virtual caffeine! ☕✨
