# Student Marks Calculator

print("===== Student Marks Calculator =====\n")

# Input number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize a list to store marks
marks = []

# Input marks for each subject
for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculate total and average
total_marks = sum(marks)
average_marks = total_marks / num_subjects

# Find highest and lowest marks
highest = max(marks)
lowest = min(marks)

# Display results
print("\n===== Results =====")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")

# Optional: Determine grade
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
else:
    
    grade = "D"

print(f"Grade: {grade}")