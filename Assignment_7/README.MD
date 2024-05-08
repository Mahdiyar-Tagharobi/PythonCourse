# Shop Inventory Management System

This Python script is a simple command-line based inventory management system for a shop. It allows the user to perform basic operations such as adding, editing, removing, searching, and buying products from the inventory.

## Features

- **Add Products**: Add new products to the inventory with unique product codes.
- **Edit Products**: Modify the details of existing products in the inventory.
- **Remove Products**: Delete products from the inventory.
- **Search Products**: Look up products by their code and name.
- **Show Product List**: Display the entire list of products in the inventory.
- **Buy Products**: Purchase products and update the inventory count.
- **Exit**: Close the application.

## How to Use

1. Run the script using a Python interpreter.
2. The main menu will be displayed with options from 1 to 7.
3. Enter the number corresponding to the action you want to perform.
4. Follow the on-screen prompts to add, edit, remove, search, or buy products.

## File Structure

- `database.txt`: Text file used to store the inventory data.
- `main.py`: The main Python script that runs the inventory management system.

## Dependencies

- `pyfiglet`: This package is used to display the ASCII art title 'Welcome to shop'. Make sure to install it using `pip install pyfiglet` before running the script.

## Note

The script uses a text file (`database.txt`) to persist data. Ensure that this file is present in the `Assignment_7` directory relative to the script.

## Disclaimer

This script is for educational purposes only. Please ensure data validation and error handling according to your use case.