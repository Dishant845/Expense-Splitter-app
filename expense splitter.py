class Participant:
    def __init__(self, name, expense):
        self.name = name
        self.expense = expense

class ExpenseSplitter:
    def __init__(self):
        self.participants = []
        self.total_expense = 0.0
        self.total_people = 0

    def input_positive_float(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print("Please enter a non-negative number.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def input_positive_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("Please enter a number greater than 0.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def set_expense_details(self):
        self.total_expense = self.input_positive_float("Enter the total expense: ")
        self.total_people = self.input_positive_int("Enter the total number of people: ")

        for i in range(self.total_people):
            name = input(f"Enter the name of person {i + 1}: ").strip()
            expense = self.input_positive_float(f"Enter the amount paid by {name}: ")
            participant = Participant(name, expense)
            self.participants.append(participant)

        print("\nInitial expense details added successfully.\n")
        self.view_balances()

    def add_participant(self):
        name = input("Enter participant's name to add: ").strip()
        expense = self.input_positive_float(f"Enter the amount paid by {name}: ")
        participant = Participant(name, expense)
        self.participants.append(participant)
        self.total_people += 1
        print(f"{name} added successfully.\n")

    def delete_participant(self):
        name = input("Enter the name of participant to delete: ").strip()
        for participant in self.participants:
            if participant.name.lower() == name.lower():
                self.participants.remove(participant)
                self.total_people -= 1
                print(f"{name} removed successfully.\n")
                return
        print("Participant not found.\n")

    def update_expense(self):
        name = input("Enter the name of participant to update expense: ").strip()
        for participant in self.participants:
            if participant.name.lower() == name.lower():
                new_expense = self.input_positive_float(f"Enter the new amount paid by {name}: ")
                participant.expense = new_expense
                print(f"{name}'s expense updated successfully.\n")
                return
        print("Participant not found.\n")

    def view_balances(self):
        if not self.participants:
            print("No participants added yet.\n")
            return

        equal_share = self.total_expense / self.total_people
        print("\n======== Final Amount to Pay ========")
        print(f"Total Expense: {self.total_expense}")
        print(f"Each Person Should Pay: {equal_share:.2f}\n")

        for participant in self.participants:
            balance = participant.expense - equal_share
            if balance > 0:
                print(f"{participant.name} should receive {balance:.2f}")
            elif balance < 0:
                print(f"{participant.name} should pay {-balance:.2f}")
            else:
                print(f"{participant.name} is settled up.")
        print()

    def menu(self):
        while True:
            print("======== Expense Splitter Menu ========")
            print("1. Add Participant")
            print("2. Delete Participant")
            print("3. Update Participant Expense")
            print("4. View Final Balances")
            print("5. Exit")
            choice = input("Enter your choice (1/2/3/4/5): ").strip()

            if choice == '1':
                self.add_participant()
            elif choice == '2':
                self.delete_participant()
            elif choice == '3':
                self.update_expense()
            elif choice == '4':
                self.view_balances()
            elif choice == '5':
                print("Thank you for using Expense Splitter!")
                break
            else:
                print("Invalid choice. Please try again.\n")


splitter = ExpenseSplitter()
splitter.set_expense_details()
splitter.menu()