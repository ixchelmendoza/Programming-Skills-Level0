import sys

class EnrollmentSystem:
    def __init__(self):
        self.users = []
        self.programs = {
            'Computer Science': {'London': 1, 'Manchester': 3, 'Liverpool': 1},
            'Medicine': {'London': 1, 'Manchester': 3, 'Liverpool': 1},
            'Marketing': {'London': 1, 'Manchester': 3, 'Liverpool': 1},
            'Arts': {'London': 1, 'Manchester': 3, 'Liverpool': 1}
        }
        self.login_attempts = 0
        self.MAX_LOGIN_ATTEMPTS = 3

    def login(self):
        while self.login_attempts < self.MAX_LOGIN_ATTEMPTS:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            # Assume a simple hardcoded username and password for the example
            if username == "user" and password == "pass":
                print("Login successful!")
                return True
            else:
                print("Incorrect username or password. Please try again.")
                self.login_attempts += 1

        print("Too many incorrect login attempts. System locked.")
        sys.exit()

    def display_programs(self):
        print("Available programs:")
        for program in self.programs:
            print(program)

    def enroll(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        self.display_programs()
        chosen_program = input("Choose a program: ")

        # Check if the chosen program is available in the selected campus
        campus_options = list(self.programs[chosen_program].keys())
        campus = input(f"Choose a campus ({', '.join(campus_options)}): ")

        if self.programs[chosen_program][campus] > 0:
            print(f"Enrollment successful for {chosen_program} at {campus} campus.")
            self.programs[chosen_program][campus] -= 1
            self.users.append({
                'first_name': first_name,
                'last_name': last_name,
                'program': chosen_program,
                'campus': campus
            })
        else:
            print(f"No available slots for {chosen_program} at {campus} campus.")
            enroll_another = input("Do you want to enroll in another campus? (yes/no): ")
            if enroll_another.lower() == 'yes':
                self.enroll()

    def run(self):
        if self.login():
            self.enroll()

if __name__ == "__main__":
    enrollment_system = EnrollmentSystem()
    enrollment_system.run()
