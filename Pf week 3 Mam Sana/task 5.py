def calculate_gpa():
    subjects = int(input("subjects in semester? "))
    
    total_grade_points = 0
    total_credits = 0
    
    for i in range(1, subjects + 1):
        print(f"\nSubject {i}:")
        gp = float(input("Grade Point (GP): "))
        ch = int(input("Credit Hours (CH): "))
        
        # Calculation formula ke mutabiq
        total_grade_points = total_grade_points + (gp * ch)
        total_credits = total_credits + ch
        
    gpa = total_grade_points / total_credits
    print("\n--- Final Result ---")
    print(" Semester GPA :", round(gpa, 2))

# Function ko chalane ke liye call kiya
calculate_gpa()