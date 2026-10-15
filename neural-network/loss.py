
def predict(weight: int, bias: int, x: int) -> int:
	return weight * x + bias

def loss(prediction: int, actual: int) -> int:
	return (prediction - actual) ** 2

inputs = [(2, 1, 2), (2, 3, 2), (1, 5, 2)]

actual=7
for w, b, x in inputs:
	p = predict(w, b, x)
	l = loss(p, 7)

	print("w=", w, "b=", b, "x=", x, "p=", p, "l=", l)


