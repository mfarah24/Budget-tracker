# Simple Budget Tracker
# This program allows the user to input income and expense transactions
# It then calculates the final balance and displays a list of all transactions

# Initialize a list to store all the transactions
transactions = []

# Initialize the balance at 0
balance = 0

# Ask the user how many transactions they would like to enter
try:
    num_transactions = int(input("How many transactions would you like to enter? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()  # Exit the program if the user input is invalid

# Loop through the number of transactions the user wants to enter
for i in range(num_transactions):
    print(f"\nEntering transaction #{i+1}")

    # Get the transaction description from the user
    description = input("Enter a description: ")

    # Get the transaction amount and convert it to a float
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount entered. Skipping this transaction.")
        continue  # Skip this transaction and continue with the next one

    # Get the type of transaction from the user
    trans_type = input("Is this income or expense? ").lower()

    # Store the transaction in a dictionary
    transaction = {
        "description": description,
        "amount": amount,
        "type": trans_type
    }

    # Add the transaction to the list
    transactions.append(transaction)

    # Update the balance based on the type
    if trans_type == "income":
        balance += amount
    elif trans_type == "expense":
        balance -= amount
    else:
        print("Invalid transaction type. Please enter 'income' or 'expense'.")

# After all transactions are entered, display the results
print("\nHere are your transactions:")
for t in transactions:
    print(f"{t['description']} ({t['type']}): ${t['amount']}")

# Display the final balance
print(f"\nFinal balance: ${balance}")
