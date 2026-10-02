# Function to calculate the average score
def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


# Function to determine the student's status
def determine_status(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Very Good"
    elif average >= 75:
        return "Passed"
    else:
        return "Failed"


# Main program
print("======================================")
print("   STUDENT ACTIVITY SCORE SYSTEM")
print("======================================")

# Ask how many students will be processed
num_students = int(input("How many students will be processed? "))

# Make sure at least 3 students are processed
while num_students < 3:
    print("You must process at least 3 students.")
    num_students = int(input("How many students will be processed? "))

# Loop through each student
for student in range(1, num_students + 1):

    print("\n--------------------------------------")
    print("Student", student)
    print("--------------------------------------")

    # Ask for student's name
    name = input("Enter student's name: ")

    # Ask for activity scores
    activity1 = float(input("Enter Activity 1 score: "))
    activity2 = float(input("Enter Activity 2 score: "))
    activity3 = float(input("Enter Activity 3 score: "))

    # Calculate average
    average = calculate_average(activity1, activity2, activity3)

    # Determine status
    status = determine_status(average)

    # Display results
    print("\n========== STUDENT RESULT ==========")
    print("Name:", name)
    print("Activity 1:", activity1)
    print("Activity 2:", activity2)
    print("Activity 3:", activity3)
    print("Average Score:", round(average, 2))
    print("Status:", status)
    print("====================================")
    
print("\nAll students have been processed.")
print("Thank you for using the Student Activity Score System!")