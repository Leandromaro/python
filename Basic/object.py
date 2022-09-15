class Circle:
	pi = 3.14

	def __init__(self, radious):
		self.radious = radious
	

	def circumference(self,):
		return 2 * Circle.pi * self.radious
	
	
	def pi(self, value):
		self.pi = value

c1 = Circle(1)
c2 = Circle(1)
c1.pi = 4.0
print(f'{c1.circumference()} {c2.circumference()}')