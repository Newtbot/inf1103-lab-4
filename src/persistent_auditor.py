from pathlib import Path
import csv



# 4. Modularity: Maintain your functional design. Create a load_inventory() and
# save_inventory() function.


# Persistence: At the start of the program, read the information previously saved
# in the inventory file. If the inventory file does not exist, start with an empty
# inventory and continue running without producing an error.
def check_file(file_path: str) -> bool:
    path = Path(file_path)
    # Check that it exists, is an actual file (not a folder), and ends with .txt
    return path.is_file() and path.suffix.lower() == ".txt"


def load_inventory():
    file = "src/model/inventory.txt"
    #check if checkfile is true if true read file or "load file"
    if check_file(file):
        with open(file, "r", encoding="utf-8") as file:
            content = file.read()
    else:
        #create file if check file is false
        with open(file, "w", encoding="utf-8") as f:
            pass
            #  f.write("Current Orders: \n\n")


# def save_inventory()



current_total = 0 # stock handle 
errors = 0 # errors 
delivery_cost = 0 # delivery cost

# 2. History Tracking: Use a Python list (array) to store every valid transaction
# amount entered.
valid_transaction = []

# 1. get_valid_input(): Handles the prompt, handles input validation, and
# returns a valid integer or a "quit" signal.
# check if stock is integer and negative value
def check_user_input(user_input):
    # isdigit only returns True for digits
    # returns false for negative
    # we should check for whether its digit or negative value
    if user_input.isdigit():
        return user_input.strip().isdigit()
    elif (user_input).lower().strip() == "quit":
        return "quit"


# 2. process_delivery(current_total, new_value): Calculates the new total and
# returns it.
def process_delivery(current_total, new_value):
    current_total+= new_value
    return current_total  # total inventory / total process stock since we always start stock at 0


# 3. calculate_tax(amount): A new requirement! This function takes a delivery
# amount and returns the tax (10% of that specific delivery).
def calculate_tax(amount):
    return round(amount * 0.1, 2)  # get 10 percent of the value and round it to 2 d.p


# 4. generate_report(total_units, failed_attempts): A dedicated function to print
# the final summary.
def generate_report(current_total, errors):
    return current_total, errors


while True:
    load_inventory()
    # 1. Initialize the inventory to zero in the start
    user_input = input("Please enter stock value: or type `quit` to kill the program: ")

    if check_user_input(user_input) == "quit":
        # 3. Write-Back: When the user types quit, save the final total and the transaction
        # history list to inventory.txt.





        total_inventory , errors = generate_report(current_total, errors)
        print("Number of Failed/Rejected Entries:", errors)
        print("Total Units Processed Inventory:" , total_inventory)
        print(valid_transaction)
        break

    #logic of my operations
    elif (check_user_input(user_input)):
        stock_value = int(user_input)
        #pass user input to process delivery for logic oprs
        current_total = process_delivery(current_total, stock_value)

        valid_transaction.append(stock_value)
        print("Total inventory:" , current_total )

        #tax calculation
        tax = calculate_tax(stock_value)
        print("Total Tax for this Delivery:"  , tax)
        # 7. Trigger Overstock Alert: If the total inventory exceeds 500 units, print an
        # alert and break the loop immediately. (keep in mind of the conditional flow we
        # discussed this week: if, elif and else)
        if (current_total > 500):
            print("My total inventory has exceeded capacity!!!")
            break

    else:
        print("Please enter a valid integer. Eg. `1` ")
        errors+=1