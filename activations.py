import math
from speech_features import speech_features
def erelu(x, alpha=1.0):
    if x >= 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)
def relu(x):
    return max(0, x)
def leaky_relu(x, alpha=0.01):
    
    if x >= 0:
        return x
    else:
        return alpha * x
print("\nLeaky ReLU outputs:")

for value in [-4.2, -3.5, -2.8, -2.1, -1.6, -1.0, -0.5, -0.2, 0.0, 0.4, 1.2, 2.5]:
    print(f"Input: {value:5.1f} -> Leaky ReLU: {leaky_relu(value):.4f}")
print("\nActivation Comparison:")

for value in speech_features:
    e = erelu(value)
    r = relu(value)
    l = leaky_relu(value)

    print(
        f"Input: {value:5.1f} | "
        f"EReLU: {e:7.4f} | "
        f"ReLU: {r:7.4f} | "
        f"Leaky ReLU: {l:7.4f}"
    )