# Importerer nødvendige moduler.
from expense import Expense
import calendar
import datetime

# Hovedfunksjonen som kjører programmet.
def main():
    print(f"Kjører Sandelu98's utgiftssporer!")
    expense_file_path = "expenses.csv"
    budget = 20000
   
    # Få input fra bruker for utgift.
    expense = get_user_expense()

   
    # Lagrer utgiften til fil (expenses.csv).
    save_expenses_to_file(expense, expense_file_path)
   
    # Leser file "expenses.csv" og regner sammen summen av utgiftene. 
    summarize_expenses(expense_file_path, budget)

# Funksjon for å få brukerens utgiftsinformasjon.
def get_user_expense():
    print(f"Henter bruker's utgift")
    expense_name = input("Skriv inn utgiftens navn: ")
    expense_amount = float(input("Skriv inn utgiftens kostnad: "))
    expense_categories = [
        "Mat", 
        "Hjem", 
        "Jobb", 
        "Morro", 
        "Misc"
    ]
    # Brukeren velger en kategori for utgiften: 1 - 5.
    while True:
        print("Velg en kategori: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Skriv inn hvilke kategori utgiften tilhører: {value_range}: ")) - 1
        
        if selected_index in range(len(expense_categories)):
            seleceted_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=seleceted_category, amount=expense_amount)
            return new_expense
        else:
            print("Ugyldig kategori. Vennligst prøv igjen!")

# Funksjon for å lagre utgiftene til fil (expenses.csv).    
def save_expenses_to_file(expense: Expense, expense_file_path):
    print(f"Lagrer brukers utgift: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
        
# Funksjon for å oppsummere utgiftene fra filen (expenses.csv).     
def summarize_expenses(expense_file_path, budget):
    print(f"Oppsummerer brukerens utgifter")
    expenses: list[Expense] = []
    
    # Leser filen og legger utgiftene til en liste.
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)
    
    # Beregner totalt beløp brukt per kategori   
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    # Skriver ut oppsummering av utgiftene.
    print("Utgiftskategorier: ")
    for key, amount in amount_by_category.items():
        print(f"      {key}: ${amount:.2f}")
    
    # Variabel som oppsummerer utgiftene slik at man ser hvor mye man har brukt hittil.    
    total_spent = sum([x.amount for x in expenses])
    print(f"Totalt brukt: ${total_spent:.2f}")
    
    # Variabel for gjenværende penger i budsjett.
    remaining_budget = budget - total_spent
    print(f"Gjenstående budsjett: ${remaining_budget:.2f}")

    # Beregner gjenværende dager i måneden.
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    # Beregner daglig budsjett.
    daily_budget = remaining_budget / remaining_days
    print(green(f"Budsjett per dag: ${daily_budget:.2f}"))
        
# Funksjon for å fargelegge tekst til grønn (eksemel brukt i daily_budget i linje 97).        
def green(text):
    return f"\033[92m{text}\033[0m"    

# Starter programmet dersom det er hovedprogrammet.    
if __name__ == "__main__":
    main()