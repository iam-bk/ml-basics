
class Neuron():

	def __init__(self, x: float, actual: float, h:float=0.0001, lr:float=0.0001):
		self.x = x
		self.actual = actual
		self.h = h
		self.lr = lr

	def predict(self, weight: float, bias: float) -> float:
		return (weight * self.x) + bias

	def miss(self, weight: float, bias: float) -> float:
		return self.predict(weight, bias) - self.actual

	def loss(self, weight: float, bias: float) -> float:
		return (self.miss(weight, bias)**2)

	def slope_w(self, weight: float, bias: float) -> float:
		return (self.loss(weight+self.h, bias) - self.loss(weight, bias)) / self.h

	def slope_b(self, weight: float, bias: float) -> float:
		return (self.loss(weight, bias+self.h) - self.loss(weight, bias)) / self.h


	def new_w(self, weight: float, slope: float) -> float:
		return weight - (slope * self.lr)

	def new_b(self, bias: float, slope: float) -> float:
		return bias - (slope * self.lr)


	def find_weight_and_bias(self, weight: int=0, bias:int=0) -> float:
		i = 0
		while True:
			loss = self.loss(weight, bias)
			slope_w = self.slope_w(weight, bias)
			slope_b = self.slope_b(weight, bias)

			print("w=", weight, "b=", bias, "loss=", loss)

			if loss <= 0.0005:
				break

			if i > 10000:
				break

			weight = self.new_w(weight, slope_w)
			bias = self.new_b(bias, slope_b)
			i = i + 1

		print("------- No of iterations --- ", i)


		return weight, bias

x=2
w=0
b=0
h=0.0001
lr=0.1
a=7
n = Neuron(x=x, actual=a, h=h, lr=lr)
print(n.find_weight_and_bias())





			
			
			
