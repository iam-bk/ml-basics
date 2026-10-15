

class Neuron():

	def __init__(self, bias: int, x: int, actual: int, h: float=0.0001, lr: float=0.1):
		self.bias = bias
		self.actual = actual
		self.h = h
		self.lr = lr
		self.x = x
		self.max_iters = 10000

	def predict(self, weight: float) -> float:
		return (weight * self.x) + self.bias

	def miss(self, weight: float) -> float:
		return self.predict(weight) - self.actual

	def loss(self, weight: float) -> float:
		return (self.predict(weight) - self.actual) ** 2

	def slope(self, weight: float) -> float:
		return (self.loss(weight + self.h) - self.loss(weight)) / self.h

	def new_weight(self, weight: float, slope: float) -> float:
		return (weight - (self.lr * slope))

	def find_weight(self, weight: float) -> float:
		for i in range(self.max_iters):
			y = self.predict(weight)
			miss = self.miss(weight)
			loss = self.loss(weight)
			slope = self.slope(weight)
			new_w = self.new_weight(weight, slope)
			
			print("prediction=", y, "miss=", miss, "loss=", loss, "slope=", slope, "new weight=", new_w)

			if loss <= 0.0005:
				break
			weight = new_w

		print("---- No of iterations it took --- ", i, ", final weight=", weight)


bias=1
x=2
actual=7
h=0.0001
lr=0.1
print("---------------------- Learning Rate::: ", lr, " --------------------------------------")
neuron = Neuron(x=x, actual=actual, h=h, lr=lr, bias=bias)
neuron.find_weight(weight=0)
lr=1.0
print("---------------------- Learning Rate::: ", lr, " --------------------------------------")
neuron1 = Neuron(x=x, actual=actual, h=h, lr=lr, bias=bias)
neuron1.find_weight(weight=0)

"""
lr=0.01
print("---------------------- Learning Rate::: ", lr, " --------------------------------------")
neuron2 = Neuron(x=x, actual=actual, h=h, lr=0.01, bias=bias)
neuron2.find_weight(weight=0)
"""	
			
