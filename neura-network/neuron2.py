
def neuron2(weight1: int, x1: int, weight2: int, x2: int, bias: int) -> int:
	return weight1*x1 + weight2 * x2 + bias

print(neuron2(2, 4, -0.5, 10, 1))
