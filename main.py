import os

DATA_FILE = "students.txt"

def ensure_datafile():
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").close()

def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def add_student():
    roll = input("Enter Roll No: ").strip()
    if not roll:
        print("Roll number can't be empty.")
        return
    # prevent duplicate roll numbers
    if find_student_line(roll) is not None:
        print("A student with this roll number already exists.")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()
    marks = input("Enter Marks: ").strip()

    with open(DATA_FILE, "a") as f:
        f.write(f"{roll},{name},{age},{course},{marks}\n")

    print("✅ Student added successfully!")

def read_all_students():
    with open(DATA_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    students = []
    for line in lines:
        parts = line.split(",")
        # in case file content malformed, skip bad lines
        if len(parts) < 5:
            continue
        students.append({
            "roll": parts[0],
            "name": parts[1],
            "age": parts[2],
            "course": parts[3],
            "marks": parts[4]
        })
    return students

def view_students():
    students = read_all_students()
    if not students:
        print("\nNo students found.")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"Roll No: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}, Marks: {s['marks']}")

def find_student_line(roll):
    """Return (index, line) of student with roll or None if not found"""
    with open(DATA_FILE, "r") as f:
        lines = [line for line in f]
    for i, line in enumerate(lines):
        parts = line.strip().split(",")
        if len(parts) >= 1 and parts[0] == roll:
            return (i, line)
    return None

def search_student():
    roll = input("Enter Roll No to search: ").strip()
    result = find_student_line(roll)
    if result is None:
        print("❌ Student not found!")
    else:
        _, line = result
        parts = line.strip().split(",")
        print(f"✅ Found: Name: {parts[1]}, Age: {parts[2]}, Course: {parts[3]}, Marks: {parts[4]}")

def update_student():
    roll = input("Enter Roll No to update: ").strip()
    found = find_student_line(roll)
    if found is None:
        print("❌ Student not found!")
        return

    index, _ = found
    students = []
    with open(DATA_FILE, "r") as f:
        students = [line for line in f]

    print("Enter new values (leave blank to keep current):")
    parts = students[index].strip().split(",")
    cur_name, cur_age, cur_course, cur_marks = parts[1], parts[2], parts[3], parts[4]

    name = input(f"Name [{cur_name}]: ").strip() or cur_name
    age = input(f"Age [{cur_age}]: ").strip() or cur_age
    course = input(f"Course [{cur_course}]: ").strip() or cur_course
    marks = input(f"Marks [{cur_marks}]: ").strip() or cur_marks

    students[index] = f"{roll},{name},{age},{course},{marks}\n"

    with open(DATA_FILE, "w") as f:
        f.writelines(students)

    print("✅ Student updated successfully!")

def delete_student():
    roll = input("Enter Roll No to delete: ").strip()
    found = find_student_line(roll)
    if found is None:
        print("❌ Student not found!")
        return

    index, _ = found
    with open(DATA_FILE, "r") as f:
        lines = [line for line in f]
    # remove the line
    del lines[index]
    with open(DATA_FILE, "w") as f:
        f.writelines(lines)
    print("✅ Student deleted successfully!")

def main():
    ensure_datafile()
    while True:
        menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()
