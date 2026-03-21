# Shaping Up
# Hint 1: In the square class, the printRow function takes in an argument i, which is not used. What happens if you
# actually use this argument?
# Hint 2: Triangles are small at the top and big at the bottom! (Huge help, I know.)
# But think about it. How can you use the variable i to print out something small at the top and big at the bottom?
# Or, heck, make an upside-down triangle! Print out something big at the top and small at the bottom.

class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	def printRow(self, i):
		for i in range(self.width):
			print(self.printChar * (i+1))

triangle = Triangle()
triangle.print()
