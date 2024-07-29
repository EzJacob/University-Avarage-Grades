# This script manages and calculates weighted averages of grades with a menu-driven interface.


def read_grades_file(filename):
    grades = []
    line_number = 0
    with open(filename, 'r') as file:
        for line in file:
            line_number += 1
            try:
                name, grade, weight = line.strip().split(':')
                name = name.strip()
                grade = grade.strip()
                weight = weight.strip()
                grades.append((name, float(grade), float(weight)))
            except ValueError:
                print(f"Error: Invalid grade or weight format '{line.strip()}' in line number: {line_number}")
            except Exception as e:
                print(f"Error: An unexpected error occurred while processing the line: '{line.strip()}' in line number {line_number}\n{e}")
    return grades


def print_grades(grades):
    if grades:
        for name, grade, weight in grades:
            print(f"{name}: Grade = {grade}, Weight = {weight}")
    else:
        print("No grades available to display.")


def calculate_weighted_average(grades):
    total_weighted_grades = sum(grade * weight for _, grade, weight in grades)
    total_weights = sum(weight for _, _, weight in grades)
    if total_weights == 0:
        raise ValueError("Total weight cannot be zero")
    return total_weighted_grades / total_weights


def calculate_weighted_average_ignoring(grades, *args):
    filtered_grades = [entry for entry in grades if entry[0] not in args]
    return calculate_weighted_average(filtered_grades)


def check_exit(user_input):
    if user_input.strip().lower() == 'exit':
        print("Exiting the program.")
        exit()


def display_menu(filepath):
    file_display = filepath if filepath else "No file path"
    print(f"\nFile: {file_display}\n")
    print("Menu:")
    print("1. Enter file name")
    print("2. Update ignore list")
    print("3. Show ignore list")
    print("4. Show grades")
    print("5. Show average")
    print("6. Show average with ignore list")
    print("7. Exit")


def main():
    print("To exit the program at any time, enter 'exit'")

    filepath = ""
    grades = []
    ignore_list = []

    while True:
        display_menu(filepath)
        choice = input("Enter your choice: ")
        check_exit(choice)

        if choice == '1':
            filepath = input("Enter the path to the file: ")
            check_exit(filepath)
            try:
                grades = read_grades_file(filepath)
                if grades:
                    print("Original Grades:")
                    print_grades(grades)
                else:
                    print("No valid grades found in the file.")
                    filepath = ""
            except Exception as e:
                print(f"Error reading file: {e}")
                filepath = ""

        elif choice == '2':
            ignores = input("Enter the names of the grades to ignore separated by commas: ")
            check_exit(ignores)
            ignore_list = [name.strip() for name in ignores.split(',') if name.strip()]
            if not ignore_list:
                print("No valid grades to ignore provided.")

        elif choice == '3':
            if ignore_list:
                print(f"Ignore List: {', '.join(ignore_list)}")
            else:
                print("Ignore list is empty.")

        elif choice == '4':
            print("Grades:")
            print_grades(grades)

        elif choice == '5':
            if grades:
                try:
                    average = calculate_weighted_average(grades)
                    print(f"\nWeighted Average: {average:.2f}")
                except ValueError as ve:
                    print(f"Error calculating weighted average: {ve}")
            else:
                print("No grades available to calculate average.")

        elif choice == '6':
            if grades:
                try:
                    new_average = calculate_weighted_average_ignoring(grades, *ignore_list)
                    print(f"\nNew Weighted Average (excluding {', '.join(ignore_list)}): {new_average:.2f}")
                except ValueError as ve:
                    print(f"Error calculating new weighted average: {ve}")
            else:
                print("No grades available to calculate average.")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()

