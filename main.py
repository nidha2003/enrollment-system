import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",      # change if needed
        password="Fathima@2003",      # add your MySQL password
        database="enrollment"
    )

# Insert student
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    if name == "" or age == "" or course == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    con = connect_db()
    cursor = con.cursor()
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    con.commit()
    con.close()

    messagebox.showinfo("Success", "Student added successfully")
    clear_fields()
    load_data()

# Delete student
def delete_student():
    selected = table.focus()
    if not selected:
        messagebox.showerror("Error", "Select a record to delete")
        return

    values = table.item(selected, "values")
    student_id = values[0]

    con = connect_db()
    cursor = con.cursor()
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    con.commit()
    con.close()

    messagebox.showinfo("Deleted", "Record deleted")
    load_data()

# Load table data
def load_data():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    con.close()

    for row in table.get_children():
        table.delete(row)

    for row in rows:
        table.insert("", tk.END, values=row)

# Clear input fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Student Enrollment Management System")
root.geometry("600x450")
root.resizable(False, False)

# Labels & Entries
tk.Label(root, text="Name:").place(x=30, y=30)
entry_name = tk.Entry(root, width=30)
entry_name.place(x=150, y=30)

tk.Label(root, text="Age:").place(x=30, y=70)
entry_age = tk.Entry(root, width=30)
entry_age.place(x=150, y=70)

tk.Label(root, text="Course:").place(x=30, y=110)
entry_course = tk.Entry(root, width=30)
entry_course.place(x=150, y=110)

# Buttons
tk.Button(root, text="Add", width=10, command=add_student).place(x=150, y=150)
tk.Button(root, text="Delete", width=10, command=delete_student).place(x=260, y=150)
tk.Button(root, text="Clear", width=10, command=clear_fields).place(x=370, y=150)

# Table
columns = ("ID", "Name", "Age", "Course")
table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)

table.place(x=20, y=200, width=560, height=230)

load_data()

root.mainloop()
