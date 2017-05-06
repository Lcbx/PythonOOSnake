#directions are set in stone
#a new object is created at each use though
#inheritance as interface is useless though thx to duck typing :/
#habits are tough


class constVec:
	def x(self):
		return 0;
	def y(self):
		return 0;
	def asTuple(self):
		return (self.x(), self.y())
	def addTo(self, tupleVec):
		X, Y = tupleVec
		X += self.x()
		Y += self.y()
		return (X, Y)

class right(constVec):
	def x(self):
		return 1;
	def y(self):
		return 0;
class left(constVec):
	def x(self):
		return -1;
	def y(self):
		return 0;
class up(constVec):
	def x(self):
		return 0;
	def y(self):
		return -1;
class down(constVec):
	def x(self):
		return 0;
	def y(self):
		return 1;