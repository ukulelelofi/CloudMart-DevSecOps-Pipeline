print("Welcome to CloudMart Solutions!")

import os

API_KEY = os.getenv("API_KEY")

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(100, 2)

print(total)
