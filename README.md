# **Student Enrollment Management System**  
A full-featured **Python (Tkinter)** application integrated with a **MySQL relational database** for managing student enrollment records.  
Designed with a clean UI, modular code structure, and efficient CRUD operations — ideal for showcasing beginner-to-intermediate Python development skills.

---

## 📘 **Overview**
The Student Enrollment Management System enables users to:

- Add new student entries  
- View all enrolled students  
- Delete selected student records  
- Clear form inputs  
- Persist all records securely in a MySQL database  

This project demonstrates practical skills in:

- GUI programming  
- Database connectivity  
- SQL  
- Backend logic  
- Python application development  

---

## 🛠️ **Tech Stack**

### **Languages & Frameworks**
- Python 3.x  
- Tkinter (GUI)

### **Database**
- MySQL  
- mysql-connector-python

### **Tools**
- VS Code  
- MySQL Workbench  
- Git & GitHub  

---

## 📁 **Project Structure**
```
enrollment-system/
│── main.py # Main application (Tkinter GUI + MySQL CRUD logic)
│── database.sql # Database schema (table creation script)
│── requirements.txt # Project dependencies
└── README.md # Project documentation
```

## 🗄️ **Database Schema**

This project uses a single table: `students`.

```sql
CREATE DATABASE IF NOT EXISTS enrollment;
USE enrollment;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(100) NOT NULL
);
```

## ⚙️ Installation & Setup Guide
Follow these steps to run the project locally:

 1. Clone the Repository
```
git clone https://github.com/<your-username>/enrollment-system.git
cd enrollment-system
```
 2. Install Dependencies
```
pip install -r requirements.txt
```
 3. Set Up MySQL Database

*Option A* — Run SQL file:
Open MySQL Workbench
Open database.sql
Click Run (⚡)

*Option B* — Copy and paste the schema manually.

 4. Configure Database Connection
Open main.py and update your database password:

```
mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="enrollment"
)
```
 5. Run the Application
Start the Tkinter GUI:
```
python main.py
```

## 🎨 Application Screenshots (Add images later)
You can insert screenshots like this:
```
![App Screenshot](screenshots/app.png)
Recommended screenshots:

Main window

Adding a student

Table populated with data
```

## 🚀 Features in Detail
✔ Add Students
Insert new student records with name, age, and course.

✔ Delete Students
Remove selected entries from both GUI and MySQL.

✔ View All Records
Automatically displays all students stored in the database.

✔ Clean, Simple GUI
Built in Tkinter, easy to navigate and beginner-friendly.

✔ Real Database Backend
Persists data using MySQL connector.

## 📌 Future Improvements
This project can be extended using:

Search student by name / ID

Update/edit student information

Export records to CSV or Excel

Add login/authentication

Replace Tkinter with PyQt or a web UI (Flask/Django)

Upload to cloud database (AWS RDS, Railway, etc.)

##👩‍💻 Author
Fathima Nidha
Beginner Python Developer | Aspiring Software Engineer
GitHub: https://github.com/nidha2003





