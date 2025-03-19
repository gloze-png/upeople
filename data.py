# Task (a): Employee List and Salary Operations

# Step 1: an employee list
employees = ["Alice Johnson", 
             "Bob Smith", 
             "Charlie Davis", 
             "David White", 
             "Emma Wilson", 
             "Fiona Clark", 
             "George Hill", 
             "Hannah Scott", 
             "Ian Wright", 
             "Jack Turner"]

# Step 2: Split into two sub-lists
subList1 = employees[:5]  # First 5 names
subList2 = employees[5:]  # Last 5 names

# Step 3:  new employee to subList2
subList2.append("Kriti Brown")

# Step 4: Remove the second employee from subList1
subList1.pop(1)  # Removes "Bob Smith"

# Step 5: Merge both lists back into one
mergedList = subList1 + subList2

# Step 6: Salary list and updating salaries
salaryList = [50000, 
              55000, 
              48000, 
              53000, 
              60000, 
              62000, 
              58000, 
              54000, 
              51000, 
              59000]  # Assume initial salaries

# Apply 4% salary increase
updatedSalaryList = [round(salary * 1.04, 2) for salary in salaryList]

# Step 7: Sort salary list and get top 3 salaries
sortedSalaries = sorted(updatedSalaryList, reverse=True)
top3Salaries = sortedSalaries[:3]

# Output Results
print("Merged Employee List:", mergedList)
print("Updated Salaries:", updatedSalaryList)
print("Top 3 Salaries:", top3Salaries)

