import numpy as np
import pandas as pd

#Student Result System
Total_marks =np.array([78,33,59,88,72,42])
Percentage = sum(Total_marks) / 600 * 100
for marks in Total_marks:
    if marks > 80:
        Grade = 'Grade A'
        break
    elif marks > 60:
        Grade = 'Grade B'
        break
    else:
        Grade = 'Grade C'
        break
print('Total Marks of the Student:',sum(Total_marks))
print('Percentage of the Student:',Percentage)
print('Grade of the Student is:',Grade)
print('Top marks of the Student:',Total_marks.max())


#Employee Salary System
employee_salary={
    'Employee_Name':['Ali','Khan','Asif','Kamal','Jamal','Luqman'],
    'Department':['IT','Health','Wapda','Education','Rescue','Navy'],
    'Salary_calculation':[90000,40000,55000,45000,52000,75000],
}
df = pd.DataFrame(employee_salary)
print('Employee Salary System')
df['Bonus']=df['Salary_calculation']*0.07
df['Total_Salary']= df['Bonus']+df['Salary_calculation']
highest_salary = df.loc[df['Total_Salary'].idxmax()]
pd.set_option('display.max_columns', None)
print(df)
print('Highest Employer Salary:\n',highest_salary)



#Attendence System
attendence = np.array([0,1,1,0,1,1,1,0,0,1,0])
present_days = np.sum(attendence)
Total_attendence = len(attendence)
absent_days = Total_attendence - present_days
attendence_percentage= present_days/Total_attendence*100

print('Total Attendence:',Total_attendence)
print('Present days:',present_days)
print('Absent days:',absent_days)
print('Total Percentage:',attendence_percentage)


#Library Management Systems
from datetime import datetime
# Create book records
books = pd.DataFrame({
    "Book_ID": [101, 102, 103, 104],
    "Title": ["Python Basics", "Data Science", "Machine Learning", "AI Fundamentals"],
    "Author": ["John", "Alice", "Bob", "David"],
    "Available": [True, True, True, True]
})

issued_books = pd.DataFrame(columns=[
    "Book_ID", "Student_Name", "Issue_Date", "Due_Date"
])

def show_available_books():
    available = books[books["Available"] == True]
    print("\nAvailable Books:")
    print(available)

def issue_book(book_id, student_name, days=7):
    global issued_books

    if book_id in books["Book_ID"].values:
        idx = books[books["Book_ID"] == book_id].index[0]
        if books.loc[idx, "Available"]:
            issue_date = datetime.now().date()
            due_date = pd.to_datetime(issue_date) + pd.Timedelta(days=days)

            issued_books.loc[len(issued_books)] = [
                book_id,
                student_name,
                issue_date,
                due_date.date()
            ]

            books.loc[idx, "Available"] = False
            print(f"Book {book_id} issued to {student_name}")
        else:
            print("Book is already issued.")
    else:
        print("Book ID not found.")

def return_book(book_id):
    global issued_books

    record = issued_books[issued_books["Book_ID"] == book_id]

    if not record.empty:
        due_date = pd.to_datetime(record.iloc[0]["Due_Date"]).date()
        return_date = datetime.now().date()

        late_days = (return_date - due_date).days
        fine = max(0, late_days * 5)  # Rs. 5 per day

        books.loc[books["Book_ID"] == book_id, "Available"] = True
        issued_books = issued_books[issued_books["Book_ID"] != book_id]

        print(f"Book {book_id} returned.")
        print(f"Fine: Rs. {fine}")
    else:
        print("No issued record found.")

def show_issued_books():
    print("\nIssued Books:")
    print(issued_books)

show_available_books()
issue_book(101, "Ali")
issue_book(103, "Sara")
show_issued_books()
return_book(101)
show_available_books()


#Bank Account Analysis
account= {
    'Months':['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'],
    'Monthly_income':[12000,15000,19000,11000,22000,9000,5000,25000,40000,33000,17000,44000],
}
df=pd.DataFrame(account)
balance = df['Monthly_income']
total_balance = sum(df['Monthly_income'])
highest_balance = df['Monthly_income'].max()
average_balance = df['Monthly_income'].mean()
print(df)
print('Total balance :',total_balance)
print('Highest balance :',highest_balance)
print('Average balance :',average_balance)


#Mobile Shop Management
mobile_shop ={
    'Mobibe_name':['Samsung A31','Oppo A1k','Tecno spark 4','iphone 17','Redmi A2','infinix hot9'],
    'Price':[33000,18000,15000,400000,90000,22000],
    'Stock':[8,12,21,5,30,33]
}
df = pd.DataFrame(mobile_shop)
print('Shop Data :\n',df)
print('Price Calculation :\n')
total_price = df['Price']*df['Stock']
print('Total Price :',sum(total_price))
print('Average Price :',total_price.mean())
print('Most Expensive Mobile :\n')
print(df.loc[df['Price'].idxmax()])
print('Stock Calculation :\n')
print('Total Stock :',df['Stock'].sum())


#Cricket Score Analysis
player_score = np.array([23,56,102,76,0,9,34,49])
total_score = np.sum(player_score)
average_score = np.mean(player_score)
highest_score = np.max(player_score)
print('Player Score of each Match :',player_score)
print('Total Score of the Player :',total_score)
print('Average Score of the Player :',average_score)
print('Highest Score of the Player :',highest_score)


#Hospital Patient Management
patient_data = {
    'Patient_Name':['Ali','Asif','Akmal','Kamal','Jamal','Salman'],
    'Patient_Age':[22,31,19,26,16,28],
    'Disease':['fever','loosemotion','temperature','stomachache','eyesinfection','skinproblem']
}
df = pd.DataFrame(data=patient_data)
print(df)
print('Patients Count :',sum(df['Patient_Name'].value_counts()))
print('Patient Age Analysis :\n')
print('Maximum Age :',df['Patient_Age'].max())
print('Minimum Age :',df['Patient_Age'].min())
print('Average Age :',df['Patient_Age'].mean())
print('Disease Statistics :\n',df['Disease'].describe())


#Exam Performance Dashboard
subject_marks ={
    'Students':['Kamal','Jamal','Asif','Sara','Khan','layeba'],
    'Math':[54,67,36,44,71,52],
    'Physics':[27,31,66,38,81,62],
    'C.S':[61,44,26,52,67,73]
}
df = pd.DataFrame(subject_marks)
print("Subject Averages:")
print("Math Average =", df["Math"].mean())
print("Physics Average =", df["Physics"].mean())
print("Computer Science Average =", df["C.S"].mean())

df["Total"] = df["Math"] + df['Physics'] + df["C.S"]

print("\nClass Average =", df["Total"].mean())

df = df.sort_values(by="Total", ascending=False)

print("\nPosition List:")
position = 1
for i in range(len(df)):
    print(position, "-", df.iloc[i]["Students"], ":", df.iloc[i]["Total"])
    position += 1


#AI Course Analysis
data = { "Name": ["Ali", "Ahmed", "Sara"],
         "Complete_topics": [8, 9, 7],
         'Total_topics':[10,10,10]}
df = pd.DataFrame(data)
df["Percentage"] = df["Complete_topics"]/df["Total_topics"]*100
print(df)
print("Topper:")
print(df[df["Complete_topics"] == df["Complete_topics"].max()])
print("\nTop Performer:")
print(df[df["Percentage"] == df["Percentage"].max()])
print('Progress Report :\n')
for i in range(len(df)):
    print(df['Name'][i],'-',df['Percentage'][i],'-% Compledted')



# University Management System
students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha",'Kashif','Khan','Asif','Jamal','Kamal','Salman']
})
print("\nStudents Data:")
print(students)

courses = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Course": ["Python", "Python", "Data Science", "Java",'C++','Java','Python','C++','Data Science','C']
})

print("\nCourse Registration:")
print(courses)

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Marks": [85, 92, 78, 88, 67, 59, 44, 61, 72, 69]
})

print("\nMarks Data:")
print(marks)

attendance = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Attendance (%)": [90, 95, 80, 85, 70, 65, 90, 60, 75, 80]
})

print("\nAttendance Data:")
print(attendance)

data = students.merge(courses, on="Student_ID")
data = data.merge(marks, on="Student_ID")
data = data.merge(attendance, on="Student_ID")

data["GPA"] = np.round((data["Marks"] / 100) * 4, 2)

print("\nComplete Student Record:")
print(data)

print("\nStudents with Marks > 80:")
print(data[data["Marks"] > 80])

print("\nStudents Sorted by GPA:")
print(data.sort_values(by="GPA", ascending=False))

print("\nAverage Marks by Course:")
print(data.groupby("Course")["Marks"].mean())

top_students = data.sort_values(by="GPA", ascending=False).head(3)

print("\nTop 3 Students:")
print(top_students[["Name", "Marks", "GPA"]])





# Banking Management System
accounts = pd.DataFrame({
    "Account_No": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "Name": ["Ali", "Sara", "Ahmed", 'Asif','Kamal','Jamal','Salman','Ayesha','sadaf','Kashif'],
    "Balance": [5000, 8000, 6000,9000,3000,12000,18000,7000,22000,11000]
})

print("Customer Accounts:")
print(accounts)

accounts.loc[accounts["Account_No"] == 11, "Balance"] += 2000
accounts.loc[accounts["Account_No"] == 13, "Balance"] -= 1000
accounts.loc[accounts["Account_No"] == 15, "Balance"] += 900
accounts.loc[accounts["Account_No"] == 17, "Balance"] -= 1500
accounts.loc[accounts["Account_No"] == 19, "Balance"] -= 2200
print("\nAfter Deposit and Withdrawal:")
print(accounts)

print("\nBalance of Account 101:")
print(accounts[accounts["Account_No"] == 11][["Name", "Balance"]])

transactions = pd.DataFrame({
    "Account_No": [11, 12],
    "Type": ["Deposit", "Withdraw"],
    "Amount": [2000, 1000]
})

print("\nTransaction History:")
print(transactions)

accounts["Interest"] = np.round(accounts["Balance"] * 0.05, 2)

print("\nInterest (5%):")
print(accounts[["Name", "Balance", "Interest"]])

accounts["Total_Balance"] = accounts["Balance"] + accounts["Interest"]

print("\nTotal Balance After Interest:")
print(accounts[["Name", "Total_Balance"]])

print("\nCustomers Sorted by Balance:")
print(accounts.sort_values(by="Balance", ascending=False))

print("\nAverage Balance:")
print(accounts["Balance"].mean())

print("\nMaximum Balance:")
print(accounts["Balance"].max())

print("\nMinimum Balance:")
print(accounts["Balance"].min())





# Hospital Management System
patients = pd.DataFrame({
    "Patient_ID": [1, 2, 3, 4, 5],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", 'Asif'],
    "Age": [25, 40, 15, 65, 30],
    "Disease": ["Fever", "Diabetes", "Fever", "Heart Disease", 'Stomachache']
})

print("Patient Records:")
print(patients)

doctors = pd.DataFrame({
    "Doctor_ID": [101, 102],
    "Doctor_Name": ["Dr. Khan", "Dr. Ahmed"],
    "Specialization": ["General", "Cardiology"]
})

print("\nDoctor Records:")
print(doctors)
appointments = pd.DataFrame({
    "Patient_ID": [1, 2, 3, 4, 5],
    "Doctor_ID": [101, 101, 101, 102, 101],
    "Date": ["2025-01-10", "2025-01-11", "2025-01-12", "2025-01-13", "2025-01-14"]
})

print("\nAppointments:")
print(appointments)

patients["Bill"] = [2000, 5000, 1500, 8000, 3000]

print("\nPatient Bills:")
print(patients[["Name", "Bill"]])

print("\nDisease Statistics:")
print(patients.groupby("Disease").size())

patients["Age_Group"] = pd.cut(
    patients["Age"],
    bins=[0, 18, 40, 100],
    labels=["Child", "Adult", "Senior"]
)

print("\nAge Group Analysis:")
print(patients[["Name", "Age", "Age_Group"]])

print("\nAverage Bill:")
print(patients["Bill"].mean())

print("\nMaximum Bill:")
print(patients["Bill"].max())

print("\nMinimum Bill:")
print(patients["Bill"].min())

print("\nAverage Age:")
print(np.mean(patients["Age"]))

print("\nMedian Age:")
print(np.median(patients["Age"]))

print("\nStandard Deviation of Age:")
print(np.std(patients["Age"]))



# E-Commerce Store Management System
products = pd.DataFrame({
    "Product_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Product_Name": ["Laptop", "Mobile", "Headphones",'Charger','Handfre','Airpod','Keyboard','Mouse','Cable','Camera'],
    "Price": [80000,40000,5000,9000,12000,14000,16000,20000,2000,6000],
    "Stock": [10,15,20,6,9,3,10,13,7,15]
})

print("Products:")
print(products)

customers = pd.DataFrame({
    "Customer_ID": [101, 102, 103],
    "Customer_Name": ["Ali", "Sara", "Ahmed"]
})

print("\nCustomers:")
print(customers)

orders = pd.DataFrame({
    "Order_ID": [1001, 1002, 1003],
    "Customer_ID": [101, 102, 103],
    "Product_ID": [1, 2, 3],
    "Quantity": [2, 1, 3]
})

print("\nOrders:")
print(orders)

for i in range(len(orders)):
    pid = orders.loc[i, "Product_ID"]
    qty = orders.loc[i, "Quantity"]

    products.loc[products["Product_ID"] == pid, "Stock"] -= qty
print("\nUpdated Inventory:")
print(products)

sales = orders.merge(products[["Product_ID", "Price"]], on="Product_ID")

sales["Revenue"] = np.round(
    sales["Quantity"] * sales["Price"], 2
)

print("\nSales Report:")
print(sales)

total_revenue = np.sum(sales["Revenue"])

print("\nTotal Revenue:")
print(total_revenue)

best_selling = sales.groupby("Product_ID")["Quantity"].sum()

print("\nBest-Selling Products:")
print(best_selling)

print("\nProducts with Stock Less Than 15:")
print(products[products["Stock"] < 15])

report = sales.groupby("Product_ID").agg({
    "Quantity": "sum",
    "Revenue": "sum"
})
print("\nProduct Sales Report:")
print(report)




# School Attendence and Result System
students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"]
})

print("Student Records:")
print(students)

attendance = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Attendance (%)": [90, 95, 85, 80]
})

print("\nAttendance:")
print(attendance)

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Math": [85, 92, 78, 88],
    "Science": [80, 90, 75, 85],
    "English": [88, 95, 70, 90]
})

print("\nMarks:")
print(marks)

data = students.merge(attendance, on="Student_ID")
data = data.merge(marks, on="Student_ID")

data["Total"] = data[["Math", "Science", "English"]].sum(axis=1)

data["Percentage"] = np.round(
    (data["Total"] / 300) * 100, 2
)

def grade(p):
    if p >= 80:
        return "A"
    elif p >= 70:
        return "B"
    elif p >= 60:
        return "C"
    else:
        return "F"

data["Grade"] = data["Percentage"].apply(grade)

data = data.sort_values(
    by="Percentage",
    ascending=False
)

data["Position"] = range(1, len(data) + 1)

print("\nAverage Percentage:")
print(np.mean(data["Percentage"]))

print("\nHighest Percentage:")
print(np.max(data["Percentage"]))

print("\nLowest Percentage:")
print(np.min(data["Percentage"]))

print("\nFinal Report:")
print(data[[
    "Name",
    "Attendance (%)",
    "Total",
    "Percentage",
    "Grade",
    "Position"
]])