
def neuron(weight: int, bias: int, x: int) -> int:
	return weight * x + bias

weight=3
bias=2
for x in range(4):
	print(neuron(weight, bias, x))

