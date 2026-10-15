
class Neuron:
	
	def __init__(self, bias: int, h: float, x: int, actual: int, lr: float):
		self.bias = bias
		self.h = h
		self.x = x
		self.lr = lr
		self.actual = actual

	def predict(self, weight: int):
		return (weight * self.x + self.bias)

	def loss(self, weight: int):
		return (self.predict(weight) - self.actual) ** 2

	def slope(self, weight: int):
		return (self.loss(weight + self.h) - self.loss(weight)) / self.h

	def calculate_weight(self, weight: int):
		return weight - self.lr * self.slope(weight)

	def run(self, weight: int, iterations: int = 5):
		for i in range(iterations):
			loss = self.loss(weight)
			slope = self.slope(weight)
			miss = self.predict(weight) - self.actual
			new_weight = self.calculate_weight(weight)

			print("weight=", weight, "loss=", loss, "slope=", slope, "miss=", miss,
			"new_weight", new_weight)
			weight = new_weight

x=2
bias=1
actual = 7
h = 0.0001
start_w = 2

n = Neuron(bias, h, x, actual, 0.1)
n.run(start_w)
print("")
print("==============")
print("")
n1 = Neuron(bias, h, x, actual, 1.0)
n1.run(start_w)
			
