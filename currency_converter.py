# Currency Converter with CRUD Operations

currency_rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.78
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in currency_rates and to_currency in currency_rates:
        return (amount / currency_rates[from_currency]) * currency_rates[to_currency]
    else:
        return None

def add_currency(code, rate):
    currency_rates[code.upper()] = rate
    print("Currency added successfully!")

def update_currency(code, rate):
    if code.upper() in currency_rates:
        currency_rates[code.upper()] = rate
        print("Currency updated successfully!")
    else:
        print("Currency not found!")

def delete_currency(code):
    if code.upper() in currency_rates:
        del currency_rates[code.upper()]
        print("Currency deleted successfully!")
    else:
        print("Currency not found!")

def display_currencies():
    print("\nAvailable Currencies:")
    for code, rate in currency_rates.items():
        print(f"{code}: {rate}")

while True:
    print("\n--- Currency Converter ---")
    print("1. Convert Currency")
    print("2. Add Currency")
    print("3. Update Currency")
    print("4. Delete Currency")
    print("5. Display Currencies")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        from_cur = input("From currency: ").upper()
        to_cur = input("To currency: ").upper()
        result = convert_currency(amount, from_cur, to_cur)
        if result:
            print(f"Converted Amount: {result:.2f}")
        else:
            print("Invalid currency code!")

    elif choice == "2":
        code = input("Currency code: ")
        rate = float(input("Rate: "))
        add_currency(code, rate)

    elif choice == "3":
        code = input("Currency code: ")
        rate = float(input("New rate: "))
        update_currency(code, rate)

    elif choice == "4":
        code = input("Currency code: ")
        delete_currency(code)

    elif choice == "5":
        display_currencies()

    elif choice == "6":
        print("Thank you for using Currency Converter!")
        break

    else:
        print("Invalid choice!")

