# 🐍 Python Practice Tasks: Conditionals & Loops

Two beginner-friendly, real-world console programs written in Python. They practise **conditional statements** and **loop structures** through realistic scenarios.

| # | Task | File | Concepts |
|---|------|------|----------|
| 1 | Student Scholarship Eligibility System | `scholarship.py` | `if`, `elif`, `else`, comparison operators, logical thinking |
| 2 | Smart Pharmacy Inventory & Sales Management System | `pharmacy_inventory.py` | `for` loop, `range()`, conditions inside loops, counters, accumulators |

---

## 📁 Project Structure

```
.
├── scholarship.py
├── pharmacy_inventory.py
└── README.md
```

## ⚙️ Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries needed

## ▶️ How to Run

```bash
python scholarship.py
python pharmacy_inventory.py
```

---

## 🎓 Task 1: Student Scholarship Eligibility System

**Topic:** Conditional Statements

### Scenario
A university awards scholarships based on academic marks, attendance and monthly family income. The program evaluates a student and prints a full report.

### Rules
- Academic marks must be **at least 80%**
- Attendance must be **at least 85%**
- Monthly family income must be **Rs. 50,000 or less**
- If all conditions are met:
  - Marks **90% or above** → **Full Scholarship**
  - Marks **80% to 89%** → **Partial Scholarship**
- If any condition fails, the program shows the **reason for ineligibility**

### Features
- Input validation (marks and attendance must be 0–100, income cannot be negative)
- Checks conditions in order and reports the first reason for ineligibility
- Prints a complete scholarship evaluation report
- Shows a congratulation message for eligible students

### Sample Run (Eligible)

```
===== SCHOLARSHIP ELIGIBILITY SYSTEM =====
Student Name: Maria
Enter academic marks (%): 92
Enter attendance percentage (%): 90
Enter monthly family income (Rs.): 40000

===== SCHOLARSHIP EVALUATION REPORT =====
Student Name: Maria
Academic Marks: 92.00%
Attendance: 90.00%
Monthly Family Income: Rs. 40000.00
Eligibility Status: Eligible
Scholarship Type: Full Scholarship
Reason: All conditions are satisfied.
Congratulations Maria! You received a Full Scholarship.
```

### Sample Run (Not Eligible)

```
Enter academic marks (%): 85
Enter attendance percentage (%): 80
Enter monthly family income (Rs.): 30000

Eligibility Status: Not Eligible
Scholarship Type: None
Reason: Attendance is less than 85%.
```

---

## 💊 Task 2: Smart Pharmacy Inventory & Sales Management System

**Topic:** Loop Structures

### Scenario
A pharmacy wants to manage its medicine inventory and calculate its daily sales revenue.

### Rules
- Ask how many different medicines need to be processed
- Use a `for` loop to process each medicine
- Collect the **medicine name, available stock, price per unit and quantity sold**
- If the requested quantity is **more than the available stock**, the sale is not processed
- If the sale succeeds, calculate the **sales amount** and **remaining stock**
- If remaining stock is **below 10 units**, show a low-stock warning and count the medicine for restocking
- Keep the **total revenue** using an accumulator
- Display a **final report**

### Features
- Input validation (empty name, negative stock, or zero/negative price or quantity skips that medicine)
- Failed sales are handled without affecting revenue
- Low-stock warnings checked for every medicine
- Counters for successful sales and restock requirements
- Final report with totals

### Sample Run

```
===== SMART PHARMACY SYSTEM =====
How many medicines do you want to process? 2

----- Medicine 1 -----
Enter medicine name: Panadol
Enter available stock: 50
Enter price per unit (Rs.): 20
Enter quantity sold: 45
Sales Amount: Rs. 900.00
Remaining Stock: 5
WARNING: Low stock for Panadol! Restocking required.

----- Medicine 2 -----
Enter medicine name: Brufen
Enter available stock: 30
Enter price per unit (Rs.): 15.5
Enter quantity sold: 10
Sales Amount: Rs. 155.00
Remaining Stock: 20

===== FINAL REPORT =====
Total Medicines Processed: 2
Successful Sales: 2
Total Revenue: Rs. 1055.00
Medicines Requiring Restocking: 1
```

---

## 🧠 What I Learned

- Writing clear decision logic with `if / elif / else`
- Validating user input before processing it
- Using `for` loops with `range()`
- Using `continue` to skip invalid entries
- Using counters and accumulators to build reports
- Formatting output with f-strings (e.g. `:.2f`)

## 👩‍💻 Author

**Maria**
Software Engineering graduate, University of Sahiwal

---

⭐ If you found this helpful, feel free to star the repository!
