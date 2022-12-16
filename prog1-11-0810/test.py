class Student:
	def __init__(self,name):
		self._name = name
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,newname):
		self._name = newname


s1 = Student("Anna")

print(s1.name)