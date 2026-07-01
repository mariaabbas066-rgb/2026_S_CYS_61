import time

# =====================================================================
# CONSTANTS & CONFIGURATIONS
# =====================================================================
CORRECT_MARKS = 4
WRONG_MARKS = -1
SKIP_MARKS = 0

# Default Credentials
ADMIN_USERNAME = "ecat_admin"
ADMIN_PASSWORD = "ecat@2024"
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "student123"

# =====================================================================
# IN-MEMORY DATA STORAGE
# =====================================================================
# Pre-seeded with 12 built-in MCQ questions
questions = [
    {"id": 1, "subject": "Math", "question": "What is the derivative of sin(x)?", "choices": ["A) cos(x)", "B) -cos(x)", "C) tan(x)", "D) sec(x)"], "answer": "A"},
    {"id": 2, "subject": "Math", "question": "What is the value of log(1)?", "choices": ["A) 1", "B) 0", "C) e", "D) 10"], "answer": "B"},
    {"id": 3, "subject": "Physics", "question": "What is the SI unit of power?", "choices": ["A) Joule", "B) Newton", "C) Watt", "D) Pascal"], "answer": "C"},
    {"id": 4, "subject": "Physics", "question": "What is the speed of light in vacuum?", "choices": ["A) 3x10^8 m/s", "B) 3x10^6 m/s", "C) 1.5x10^8 m/s", "D) 3x10^10 m/s"], "answer": "A"},
    {"id": 5, "subject": "Chemistry", "question": "What is the pH of pure water?", "choices": ["A) 0", "B) 5", "C) 7", "D) 14"], "answer": "C"},
    {"id": 6, "subject": "Chemistry", "question": "Which gas is known as laughing gas?", "choices": ["A) NO2", "B) N2O", "C) NO", "D) N2O5"], "answer": "B"},
    {"id": 7, "subject": "Computer", "question": "Which of the following is an in-memory linear data structure?", "choices": ["A) Graph", "B) Tree", "C) Array/List", "D) Hash Table"], "answer": "C"},
    {"id": 8, "subject": "Computer", "question": "What is the time complexity of searching in a Balanced BST?", "choices": ["A) O(1)", "B) O(n)", "C) O(n log n)", "D) O(log n)"], "answer": "D"},
    {"id": 9, "subject": "Math", "question": "If 2x + 5 = 15, then x = ?", "choices": ["A) 5", "B) 10", "C) 2", "D) 4"], "answer": "A"},
    {"id": 10, "subject": "Physics", "question": "Which law states that F = ma?", "choices": ["A) 1st Law", "B) 2nd Law", "C) 3rd Law", "D) Law of Gravitation"], "answer": "B"},
    {"id": 11, "subject": "Chemistry", "question": "What is the chemical formula of Salt?", "choices": ["A) HCl", "B) NaOH", "C) NaCl", "D) H2O"], "answer": "C"},
    {"id": 12, "subject": "Computer", "question": "Which language is primarily used for Data Science?", "choices": ["A) HTML", "B) Python", "C) CSS", "D) Assembly"], "answer": "B"}
]

all_results = []  # Stores all student exam records

# =====================================================================
# CORE UTILITY FUNCTIONS
# =====================================================================
def calculate_grade(percentage):
    if percentage >= 80:
        return "EXCELLENT"
    elif percentage >= 65:
        return "GOOD"
    elif percentage >= 50:
        return "AVERAGE"
    else:
        return "BELOW AVERAGE"

def login_portal(required_username, required_password, role_name):
    print(f"\n--- {role_name} Login ---")
    attempts = 3
    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username == required_username and password == required_password:
            print("\nLogin Successful! Please wait...")
            time.sleep(1)
            return True
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts remaining: {attempts}")
    
    print(f"\n[LOCKOUT] Too many failed attempts. {role_name} Portal is locked.")
    return False

# =====================================================================
# ADMIN PORTAL FEATURES (8 Options)
# =====================================================================
def view_all_questions():
    print("\n--- Question Bank ---")
    if not questions:
        print("Question bank is empty.")
        return
    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}. [{q['subject']}] {q['question']}")
        for choice in q['choices']:
            print(f"  {choice}")
        print(f"  Correct Answer: {q['answer']}")

def add_new_question():
    print("\n--- Add New Question ---")
    subject = input("Enter Subject (e.g., Math, Physics): ").strip()
    q_text = input("Enter Question Text: ").strip()
    
    choices = []
    for char in ['A', 'B', 'C', 'D']:
        choice_text = input(f"Enter Choice {char}: ").strip()
        choices.append(f"{char}) {choice_text}")
        
    while True:
        correct = input("Enter Correct Choice (A, B, C, or D): ").strip().upper()
        if correct in ['A', 'B', 'C', 'D']:
            break
        print("Invalid choice! Choose from A, B, C, or D.")
        
    new_id = questions[-1]['id'] + 1 if questions else 1
    questions.append({
        "id": new_id,
        "subject": subject,
        "question": q_text,
        "choices": choices,
        "answer": correct
    })
    print("\nQuestion Added Successfully!")

def delete_question():
    view_all_questions()
    if not questions:
        return
    print("\n--- Delete Question ---")
    try:
        q_num = int(input("Enter Question Number to delete: "))
        if 1 <= q_num <= len(questions):
            removed = questions.pop(q_num - 1)
            print(f"\nRemoved Question: {removed['question']}")
        else:
            print("Invalid question number.")
    except ValueError:
        print("Please enter a valid integer number.")

def question_bank_statistics():
    print("\n--- Question Bank Statistics ---")
    total_q = len(questions)
    print(f"Total Questions: {total_q}")
    
    stats = {}
    for q in questions:
        sub = q['subject']
        stats[sub] = stats.get(sub, 0) + 1
        
    print("Breakdown by Subject:")
    for sub, count in stats.items():
        print(f" - {sub}: {count}")

def view_all_student_results():
    print("\n--- All Student Results ---")
    if not all_results:
        print("No student records found.")
        return
        
    print(f"{'No.':<4} {'Name':<15} {'Roll No':<10} {'Score':<8} {'Percentage':<12} {'Grade':<15} {'Time':<20}")
    print("-" * 85)
    for idx, r in enumerate(all_results, 1):
        print(f"{idx:<4} {r['name']:<15} {r['roll']:<10} {r['score']:<8} {r['percentage']:.2f}%     {r['grade']:<15} {r['time']}")

def view_detailed_result():
    view_all_student_results()
    if not all_results:
        return
    try:
        idx = int(input("\nEnter Attempt Number to drill down: ")) - 1
        if 0 <= idx < len(all_results):
            res = all_results[idx]
            print(f"\n=== Detailed Result for {res['name']} ({res['roll']}) ===")
            print(f"Total Score: {res['score']} | Percentage: {res['percentage']:.2f}% | Grade: {res['grade']}")
            print("-" * 50)
            
            for item in res['detailed_review']:
                print(f"\nQ: {item['question']}")
                print(f"   Your Answer: {item['student_ans']} | Correct Answer: {item['correct_ans']}")
                print(f"   Status: {item['status']} ({item['marks_earned']} Marks)")
        else:
            print("Invalid record selection.")
    except ValueError:
        print("Invalid Input.")

def class_result_statistics():
    print("\n--- Class Result Statistics ---")
    if not all_results:
        print("No data available to calculate statistics.")
        return
        
    scores = [r['score'] for r in all_results]
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    
    pass_count = sum(1 for r in all_results if r['percentage'] >= 50)
    fail_count = len(all_results) - pass_count
    
    grade_dist = {"EXCELLENT": 0, "GOOD": 0, "AVERAGE": 0, "BELOW AVERAGE": 0}
    for r in all_results:
        grade_dist[r['grade']] += 1
        
    print(f"Highest Score: {highest}")
    print(f"Lowest Score:  {lowest}")
    print(f"Average Score: {average:.2f}")
    print(f"Passed Students (>=50%): {pass_count}")
    print(f"Failed Students (<50%):  {fail_count}")
    print("\nGrade Distribution:")
    for grade, cnt in grade_dist.items():
        print(f" - {grade}: {cnt}")

def admin_portal():
    if not login_portal(ADMIN_USERNAME, ADMIN_PASSWORD, "Admin Portal"):
        return
        
    while True:
        print("\n=== ECAT ADMIN PORTAL ===")
        print("1. View All Questions")
        print("2. Add New Question")
        print("3. Delete Question")
        print("4. Question Bank Statistics")
        print("5. View All Student Results")
        print("6. View Detailed Result (Per Student)")
        print("7. Class Result Statistics")
        print("8. Logout")
        
        choice = input("Select an option (1-8): ").strip()
        if choice == '1': view_all_questions()
        elif choice == '2': add_new_question()
        elif choice == '3': delete_question()
        elif choice == '4': question_bank_statistics()
        elif choice == '5': view_all_student_results()
        elif choice == '6': view_detailed_result()
        elif choice == '7': class_result_statistics()
        elif choice == '8': 
            print("Logging out from Admin Portal...")
            break
        else:
            print("Invalid choice, try again.")

# =====================================================================
# STUDENT PORTAL FEATURES (3 Options)
# =====================================================================
def view_exam_rules():
    print("\n=== ECAT EXAM RULES & INSTRUCTIONS ===")
    print(f"1. Total Questions available: {len(questions)}")
    print(f"2. Marking Scheme:")
    print(f"   - Correct Answer: +{CORRECT_MARKS} Marks")
    print(f"   - Wrong Answer:   {WRONG_MARKS} Mark")
    print(f"   - Skipped Question:{SKIP_MARKS} Marks")
    print("3. Navigation:")
    print("   - Type 'A', 'B', 'C', or 'D' to submit your response.")
    print("   - Type 'S' to skip the current question.")
    print("   - Type 'SUBMIT' at any stage to finish and exit early.")
    print("=" * 38)

def start_exam(student_name, student_roll):
    if len(questions) < 10:
        print("\n[ERROR] System cannot start exam. Question Bank must have at least 10 questions.")
        return

    print("\nInitializing Exam... Good Luck!")
    answers = {}  # {question_index: 'A'/'B'/'C'/'D'/'S'}
    
    for idx in range(len(questions)):
        q = questions[idx]
        print(f"\nQuestion {idx + 1} of {len(questions)} [{q['subject']}]")
        print(q['question'])
        for choice in q['choices']:
            print(f"  {choice}")
            
        while True:
            ans = input("Your Answer (A/B/C/D), 'S' to skip, or 'SUBMIT' to finish: ").strip()
            if ans.upper() in ['A', 'B', 'C', 'D', 'S', 'SUBMIT']:
                break
            print("Invalid entry! Enter A, B, C, D, S or SUBMIT.")
            
        if ans.upper() == 'SUBMIT':
            print("\nSubmitting exam early as requested...")
            break
            
        answers[idx] = ans.upper()
    
    # Post-Exam Calculations & Review Generator
    correct_cnt = 0
    wrong_cnt = 0
    skip_cnt = 0
    detailed_review = []
    
    for idx in range(len(questions)):
        q = questions[idx]
        student_ans = answers.get(idx, 'S')  # Defaults to Skip if early submitted
        correct_ans = q['answer']
        
        if student_ans == 'S':
            status = "Skipped"
            marks = SKIP_MARKS
            skip_cnt += 1
        elif student_ans == correct_ans:
            status = "Correct"
            marks = CORRECT_MARKS
            correct_cnt += 1
        else:
            status = "Wrong"
            marks = WRONG_MARKS
            wrong_cnt += 1
            
        detailed_review.append({
            "question": q['question'],
            "student_ans": student_ans,
            "correct_ans": correct_ans,
            "status": status,
            "marks_earned": marks
        })
        
    total_score = (correct_cnt * CORRECT_MARKS) + (wrong_cnt * WRONG_MARKS) + (skip_cnt * SKIP_MARKS)
    max_possible_score = len(questions) * CORRECT_MARKS
    percentage = (total_score / max_possible_score) * 100 if max_possible_score > 0 else 0
    grade = calculate_grade(percentage)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Save student record in memory
    all_results.append({
        "name": student_name,
        "roll": student_roll,
        "score": total_score,
        "percentage": percentage,
        "grade": grade,
        "time": current_time,
        "detailed_review": detailed_review
    })
    
    # Instant Result Display
    print("\n================================")
    print("         EXAM RESULTS           ")
    print("================================")
    print(f"Name:        {student_name}")
    print(f"Roll Number: {student_roll}")
    print(f"Total Score: {total_score} / {max_possible_score}")
    print(f"Percentage:  {percentage:.2f}%")
    print(f"Grade:       {grade}")
    print("--------------------------------")
    print(f"Correct: {correct_cnt} | Wrong: {wrong_cnt} | Skipped: {skip_cnt}")
    print("================================")

def student_portal():
    if not login_portal(STUDENT_USERNAME, STUDENT_PASSWORD, "Student Portal"):
        return
        
    print("\n--- Registration Details ---")
    student_name = input("Enter Full Name: ").strip()
    student_roll = input("Enter Roll Number: ").strip()
    
    while True:
        print(f"\n=== WELCOME {student_name.upper()} ({student_roll}) ===")
        print("1. View Exam Rules")
        print("2. Start Exam")
        print("3. Logout")
        
        choice = input("Select an option (1-3): ").strip()
        if choice == '1':
            view_exam_rules()
        elif choice == '2':
            start_exam(student_name, student_roll)
            print("\nReturning to main menu...")
        elif choice == '3':
            print("Logging out from Student Portal...")
            break
        else:
            print("Invalid choice, try again.")

# =====================================================================
# MAIN PORTAL SWITCH / ENTRY POINT
# =====================================================================
def main():
    while True:
        print("\n========================================")
        print("   ECAT EXAM APPLICATION SYSTEM   ")
        print("========================================")
        print("1. Access Admin Portal")
        print("2. Access Student Portal")
        print("3. Shutdown System")
        print("========================================")
        
        portal_choice = input("Select Portal option (1-3): ").strip()
        if portal_choice == '1':
            admin_portal()
        elif portal_choice == '2':
            student_portal()
        elif portal_choice == '3':
            print("\nShutting down the application. Goodbye!")
            break
        else:
            print("Invalid selection. Please type 1, 2, or 3.")

if __name__ == "__main__":
    main()