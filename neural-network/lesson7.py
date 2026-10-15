from dataclasses import dataclass


@dataclass
class NeuronInput:
	x: float
	a: float

class Neuron():

	def __init__(self, h: float=0.0001, lr: float=0.1):
		self.h = h
		self.lr = lr

	def predict(self, weight: float, bias: float, i: NeuronInput) -> float:
		return (weight * i.x) + bias

	def miss(self, weight: float, bias: float, i: NeuronInput) -> float:
		return self.predict(weight, bias, i) - i.a

	def loss(self, weight: float, bias: float, i: NeuronInput) -> float:
		return (self.miss(weight, bias, i)) ** 2

	def batch_loss(self, weight: float, bias: float, i: NeuronInput, j: NeuronInput) -> float:
		loss_i = self.loss(weight, bias, i)
		loss_j = self.loss(weight, bias, j)
		return (loss_i + loss_j) / 2

	def slope_w(self, weight: float, bias: float, i: NeuronInput, j: NeuronInput) -> float:
		loss = self.batch_loss(weight, bias, i, j)
		loss_h = self.batch_loss(weight + self.h, bias, i, j)
		return (loss_h - loss) / self.h
	
	def slope_b(self, weight: float, bias: float, i: NeuronInput, j: NeuronInput) -> float:
		loss = self.batch_loss(weight, bias, i, j)
		loss_h = self.batch_loss(weight, bias + self.h, i, j)
		return (loss_h - loss) / self.h

	def _print_run(self, weight: float, bias: float, i: NeuronInput):
		p = self.predict(weight, bias, i)
		miss = self.miss(weight, bias, i)
		loss = self.loss(weight, bias, i)

		print("predict=", p, "miss=", miss, "loss=", loss)


	def run(self, i: NeuronInput, j: NeuronInput) -> (float, float):
		max_runs = 10000
		weight = 0
		bias = 0
		t = 0

		while True:
			loss = self.batch_loss(weight, bias, i, j)
			slope_w = self.slope_w(weight, bias, i, j)
			slope_b = self.slope_b(weight, bias, i, j)
			print("---------- Row0 --------------")
			self._print_run(weight, bias, i)
			print("------------Row1 --------------")
			self._print_run(weight, bias, j)

			if loss <= 0.0005:
				break

			if t >= max_runs:
				break

			weight = weight - (slope_w * self.lr)
			bias = bias - (slope_b * self.lr)
			t = t + 1

			print("loss=", loss, "slope_w=", slope_w, "slope_b=", slope_b)

		print("Number of iterations ----", t)

		return weight, bias


neuron = Neuron()
inputs = [NeuronInput(1, 3), NeuronInput(2, 7)]
weight, bias = neuron.run(inputs[0], inputs[1])
print("Frozen Weight", weight, "Frozen Bias", bias)
			
		

		
		
		
