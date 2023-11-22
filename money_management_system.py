import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# predefined categories
categories = ["housing", "grocery", "transportation", "car", "dinner", "travel", "entertainment", "education"]

def calculate_remaining():
    total_income = int(salary_entry.get()) + int(additional_income_entry.get())
    total_expenses = sum(int(entry.get()) for entry in expense_entries)
    remaining = total_income - total_expenses
    remaining_var.set(f"Remaining: {remaining}")
    draw_piechart([int(entry.get()) for entry in expense_entries], remaining)
    display_table(total_income, [int(entry.get()) for entry in expense_entries], remaining)

def draw_piechart(expenses, remaining):
    # Create a new tkinter window
    new_window = tk.Toplevel(root)
    figure = plt.Figure(figsize=(5,5), dpi=100)
    ax = figure.add_subplot(111)
    pie = FigureCanvasTkAgg(figure, new_window)
    pie.get_tk_widget().pack()
    # Include remaining money in the pie chart
    expenses.append(remaining)
    labels = categories + ["remaining"]
    ax.pie(expenses, labels=labels, autopct='%1.1f%%')
    ax.set_title('Expense Distribution')

def display_table(total_income, expenses, remaining):
    # Create a new tkinter window
    new_window = tk.Toplevel(root)
    tree = ttk.Treeview(new_window, columns=('Income/Expense', 'Amount'), show='headings')
    tree.heading('Income/Expense', text='Income/Expense')
    tree.heading('Amount', text='Amount')
    tree.pack()
    # Insert income and expenses into the table
    tree.insert('', 'end', values=('Salary', salary_entry.get()))
    tree.insert('', 'end', values=('Additional Income', additional_income_entry.get()))
    for category, expense in zip(categories, expenses):
        tree.insert('', 'end', values=(category, expense))
    tree.insert('', 'end', values=('Remaining', remaining))

root = tk.Tk()

salary_var = tk.StringVar()
salary_var.set("Enter Salary")
salary_label = tk.Label(root, textvariable=salary_var)
salary_label.grid(row=0, column=0)
salary_entry = tk.Entry(root)
salary_entry.grid(row=0, column=1)

additional_income_var = tk.StringVar()
additional_income_var.set("Enter Additional Income (Optional)")
additional_income_label = tk.Label(root, textvariable=additional_income_var)
additional_income_label.grid(row=1, column=0)
additional_income_entry = tk.Entry(root)
additional_income_entry.grid(row=1, column=1)

expense_entries = []
for i, category in enumerate(categories, start=2):
    category_var = tk.StringVar()
    category_var.set(category)
    category_label = tk.Label(root, textvariable=category_var)
    category_label.grid(row=i, column=0)
    expense_entry = tk.Entry(root)
    expense_entry.grid(row=i, column=1)
    expense_entries.append(expense_entry)

calculate_button = tk.Button(root, text="Calculate Remaining", command=calculate_remaining)
calculate_button.grid(row=len(categories)+2, column=0)

remaining_var = tk.StringVar()
remaining_var.set("Remaining: ")
remaining_label = tk.Label(root, textvariable=remaining_var)
remaining_label.grid(row=len(categories)+2, column=1)

root.mainloop()

