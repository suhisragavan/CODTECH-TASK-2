class GradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)
        print(f"Grade {grade} added for {subject}.")

    def calculate_average(self):
        total, count = 0, 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0

    def calculate_gpa(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 4.0
        elif avg >= 80:
            return 3.0
        elif avg >= 70:
            return 2.0
        elif avg >= 60:
            return 1.0
        else:
            return 0.0

    def letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def display_summary(self):
        print("\nGrade Summary:")
        for subject, grades in self.grades.items():
            avg = sum(grades) / len(grades) if grades else 0
            print(f"{subject}: Grades: {grades}, Average: {avg:.2f}")
        overall_avg = self.calculate_average()
        print(f"\nOverall Average: {overall_avg:.2f}")
        print(f"Overall Letter Grade: {self.letter_grade()}")
        print(f"GPA: {self.calculate_gpa():.2f}")


def main():
    tracker = GradeTracker()
    while True:
        print("\n1. Add Grade")
        print("2. Display Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade (0-100): "))
                if 0 <= grade <= 100:
                    tracker.add_grade(subject, grade)
                else:
                    print("Please enter a valid grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
        elif choice == '2':
            tracker.display_summary()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
