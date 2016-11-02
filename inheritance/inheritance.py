class Parent():
	"""docstring for Parent"""
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last name: " + self.last_name)
		print("Eye Color: " + self.eye_color)

class Child(Parent):
	"""docstring for Child"""
	def __init__(self, last_name, eye_color, toys):
		Parent.__init__(self, last_name, eye_color)
		self.toys = toys

	def show_info(self):
		print("Last name: " + self.last_name)
		print("Eye Color: " + self.eye_color)
		print("Toys: " + str(self.toys))		

billy_cyrus = Parent("Cyrus", "blue")
#print(billy_cyrus.last_name)
#billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "Blue", 5)
#print(miley_cyrus.last_name)		
#print(miley_cyrus.toys)
miley_cyrus.show_info()		