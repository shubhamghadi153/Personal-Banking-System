# Class based banking system
import json

class transaction:
    def __init__(self, title, amount, type, note=""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note
    
    def display_info(self):
        return f"transaction: \n Expense: {self.title}\n Amount: {self.amount}\n Type: {self.type}\n Note: {self.note}"

class Bank:
    def __init__(self):
        self.wallet = []

    # Add
    def add_transaction(self, transaction):
        self.wallet.append(transaction)

    # Remove
    def del_transaction(self, title):
        for trans in self.wallet:
            if trans.title == title:
                self.wallet.remove(trans)
                return f"{title} has been removed!"
        return f"{title} is not found..."

    # Display all
    def display(self):
        if not self.wallet:
            return "No transaction available in your wallet."
        return "\n".join([trans.display_info() for trans in self.wallet])

    # Search
    def search_wallet(self, query):
        found = [trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]
        if not found:
            return "No transactions!"
        return "\n".join([trans.display_info() for trans in found])

    # Save
    def save_file(self, filename="wallet.json"):
        data = [{'Expense': trans.title, 'Amount': trans.amount, 'Type': trans.type, 'Note': trans.note} for trans in self.wallet]
        with open(filename, "w") as file:
            json.dump(data, file)

    # Load
    def load_file(self, filename="wallet.json"):
        try:
            with open(filename, "r") as file:
                data = file.read()
                if not data:  # Check if file is empty
                    print("The file is empty.")
                    return
                data = json.loads(data)
                self.wallet = [transaction(trans['title'], trans['amount'], trans['type'], trans['note']) for trans in data]
        except FileNotFoundError:
            print("We don't have that file...")
        except json.JSONDecodeError:
            print("Error decoding JSON. The file might be corrupted.")

def main():
    wallet = Bank()
    
    while True:
        print("\n=== Personal Banking System ===")
        print("1. Add a Transaction")
        print("2. Remove a Transaction")
        print("3. Display All Transactions")
        print("4. Search For Transaction")
        print("5. Save Transactions to File")
        print("6. Load Transactions from File")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            title = input("Enter the Title: ")
            amount = float(input("Enter the amount: "))
            type = input("Expense or Deposit: ")
            trans = transaction(title, amount, type)
            wallet.add_transaction(trans)
            print(f"{title} added successfully!")
        
        elif choice == "2":
            title = input("Enter the Title: ")
            print(wallet.del_transaction(title))
        
        elif choice == "3":
            print(wallet.display())
        
        elif choice == "4":
            query = input("Enter the title: ")
            print(wallet.search_wallet(query))
        
        elif choice == "5":
            wallet.save_file()
            print("Saved as JSON")
        
        elif choice == "6":
            wallet.load_file()
            print("Loaded JSON")
        
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid Choice, Please try again.")

if __name__ == "__main__":
    main()
