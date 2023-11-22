# A money management system in Python

# Define a function to get user input for money in
def money_in():
    # Initialize an empty dictionary to store money in categories and amounts
    money_in_dict = {}
    # Ask the user to enter their weekly paychecks and additional incomess
    print("Please enter your weekly paychecks and additional income:")
    # Use a while loop to get user input until they enter "done"
    while True:
        # Get the category name from the user
        category = input("Enter the category name (e.g. salary, bonus, etc.) or 'done' to finish: ")
        # If the user enters "done", break the loop
        if category.lower() == "done":
            break
        # Otherwise, get the amount from the user
        else:
            # Use a try-except block to handle invalid input
            try:
                # Convert the input to a float
                amount = float(input(f"Enter the amount for {category}: "))
                # Add the category and amount to the dictionary
                money_in_dict[category] = amount
            except ValueError:
                # Print an error message and continue the loop
                print("Invalid input. Please enter a valid number.")
                continue
    # Return the money in dictionary
    return money_in_dict

# Define a function to get user input for money out
def money_out():
    # Initialize an empty dictionary to store money out categories and amounts
    money_out_dict = {}
    # Define a list of fixed categories for money out
    fixed_categories = ["housing", "grocery", "transportation", "car", "dinner", "travel", "entertainment", "education"]
    # Ask the user to enter their money out for each fixed category
    print("Please enter your money out for each category:")
    # Use a for loop to iterate over the fixed categories
    for category in fixed_categories:
        # Use a try-except block to handle invalid input
        try:
            # Convert the input to a float
            amount = float(input(f"Enter the amount for {category}: "))
            # Add the category and amount to the dictionary
            money_out_dict[category] = amount
        except ValueError:
            # Print an error message and continue the loop
            print("Invalid input. Please enter a valid number.")
            continue
    # Ask the user to enter any other categories and amounts for money out
    print("Please enter any other categories and amounts for money out:")
    # Use a while loop to get user input until they enter "done"
    while True:
        # Get the category name from the user
        category = input("Enter the category name (e.g. clothes, gifts, etc.) or 'done' to finish: ")
        # If the user enters "done", break the loop
        if category.lower() == "done":
            break
        # Otherwise, get the amount from the user
        else:
            # Use a try-except block to handle invalid input
            try:
                # Convert the input to a float
                amount = float(input(f"Enter the amount for {category}: "))
                # Add the category and amount to the dictionary
                money_out_dict[category] = amount
            except ValueError:
                # Print an error message and continue the loop
                print("Invalid input. Please enter a valid number.")
                continue
    # Return the money out dictionary
    return money_out_dict

# Define a function to calculate the total money in and money out
def total_money(money_dict):
    # Initialize a variable to store the total amount
    total = 0
    # Use a for loop to iterate over the values in the dictionary
    for value in money_dict.values():
        # Add the value to the total
        total += value
    # Return the total amount
    return total

# Define a function to display the money in and money out tables
def display_tables(money_in_dict, money_out_dict):
    # Import the tabulate module to create tables
    import tabulate
    # Create a list of lists to store the money in table data
    money_in_table = []
    # Use a for loop to iterate over the items in the money in dictionary
    for item in money_in_dict.items():
        # Append the item as a list to the money in table data
        money_in_table.append(list(item))
    # Calculate the total money in
    total_in = total_money(money_in_dict)
    # Append the total money in as a list to the money in table data
    money_in_table.append(["Total", total_in])
    # Create a list of lists to store the money out table data
    money_out_table = []
    # Use a for loop to iterate over the items in the money out dictionary
    for item in money_out_dict.items():
        # Append the item as a list to the money out table data
        money_out_table.append(list(item))
    # Calculate the total money out
    total_out = total_money(money_out_dict)
    # Append the total money out as a list to the money out table data
    money_out_table.append(["Total", total_out])
    # Print the money in table with a header and a border
    print(tabulate.tabulate(money_in_table, headers=["Money In", "Amount"], tablefmt="fancy_grid"))
    # Print a blank line
    print()
    # Print the money out table with a header and a border
    print(tabulate.tabulate(money_out_table, headers=["Money Out", "Amount"], tablefmt="fancy_grid"))
    # Return the total money in and money out
    return total_in, total_out

# Define a function to display the money left over and the chart of the spendings and remaining money
def display_money_left_over_and_chart(total_in, total_out):
    # Import the matplotlib.pyplot module to create a chart
    import matplotlib.pyplot as plt
    # Calculate the money left over
    money_left_over = total_in - total_out
    # Print the money left over
    print(f"Money left over: {money_left_over}")
    # Create a list of labels for the chart
    labels = ["Money In", "Money Out", "Money Left Over"]
    # Create a list of values for the chart
    values = [total_in, total_out, money_left_over]
    # Create a list of colors for the chart
    colors = ["green", "red", "blue"]
    # Create a pie chart with the labels, values, and colors
    plt.pie(values, labels=labels, colors=colors, autopct="%1.1f%%")
    # Show the chart
    plt.show()

# Call the money in function and store the result in a variable
money_in_dict = money_in()
# Call the money out function and store the result in a variable
money_out_dict = money_out()
# Call the display tables function and store the results in variables
total_in, total_out = display_tables(money_in_dict, money_out_dict)
# Call the display money left over and chart function with the results
display_money_left_over_and_chart(total_in, total_out)
