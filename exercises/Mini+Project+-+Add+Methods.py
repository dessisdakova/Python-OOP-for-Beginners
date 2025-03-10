import json


class MusicSchool:

	students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Cello"]],
                "Eric":   [12, "583-356-223", ["Singing"]]}


	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

	# Add your methods below this line
	def print_students_data(self):
		for key, value in MusicSchool.students.items():
			self.print_student(key)

	def print_student(self, name: str):
		for key, value in MusicSchool.students.items():
			if name == key:
				age = value[0]
				courses = value[2]
				print(f"Student: {name} who is {age} years old and is taking {courses}")

	def add_student(self, name: str, data: list):
		MusicSchool.students[name] = data
		self.save_students_to_file()

	def save_students_to_file(self):
		with open("students.txt", "w") as file:
			json.dump(MusicSchool.students, file)
			print("Students data is saved to a file.")

	def load_students_from_file(self):
		try:
			with open("students.txt", "r") as file:
				MusicSchool.students = json.load(file)
				print("Students data loaded from file.")
		except FileNotFoundError:
			print("No previous data found.")

# Create the instance
school = MusicSchool(8, 1500)

# Call the methods
school.load_students_from_file()
school.add_student("Jack", [60, "562-234-234", ["Piano"]])
school.print_students_data()
