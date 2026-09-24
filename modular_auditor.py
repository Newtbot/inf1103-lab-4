# Week 2 Requirements
"""
1. Initialize the inventory to zero in the start
2. Run in a continuous loop asking user to enter a stock quantity, until the
user types quit.
3. If the user enters a valid value:
• Add the delivery amount to the running total.
• Calculate the tax for that delivery.
• Update any counters and records you are tracking, such as the number
of deliveries processed.
4. Reporting: When the user types quit, print the Total Deliveries Processed
and the Number of Failed/Rejected Entries.
"""

current_total = 0 # stock handle 
errors = 0 # errors 
delivery_cost = 0 # delivery cost


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
    # 1. Initialize the inventory to zero in the start
    user_input = input("Please enter stock value: or type `quit` to kill the program: ")

    if check_user_input(user_input) == "quit":
        total_inventory , errors = generate_report(current_total, errors)
        print("Number of Failed/Rejected Entries:", errors)
        print("Total Units Processed Inventory:" , total_inventory)
        break

    #logic of my operations
    elif (check_user_input(user_input)):
        stock_value = int(user_input)
        #pass user input to process delivery for logic oprs
        current_total = process_delivery(current_total, stock_value)
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