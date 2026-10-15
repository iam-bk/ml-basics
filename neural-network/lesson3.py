"""
 y = w * x + b 

 # y is the value we are predicting 

 w - weight 
 x - input 
 b - bias 
 a - actual 

 Now, when we predict a value, we want to know how close the prediction is from the value. To calculate that, we need to find a loss 

 loss = (pred - actual) ^ 2

 We are using square for two reasons, one we want to remove signs (+ve, -ve) to be sure zero can be trusted, second penalising the error rate. 

 bias - is where to begin
 
 Now, we have to find the right weight. To find the right weight, if we nudge w by a little, does loss  fall or rise, is it going upwards or downwards, the value shows how steep it is. It is called slope

 slope = [ loss(w + h) - loss(w)]/h

 h = 1

 ---
 x=2
 b=1
 actual=7

  y = w * 2 + 1
  y = 2w + 1
  
  loss = (2w + 1 - 7)^2
  loss = (2w - 6)^2
"""

def loss(weight: int) -> int:
	return (2*weight - 6) ** 2

def slope(weight: int, h: float) -> int:
	return (loss(weight + h) - loss(weight)) / h

h=0.0001
for w in range(5):
	print("weight=", w, "loss=", loss(w), "slope=", slope(w, h))
