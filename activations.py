import math
def erelu(x, alpha=1.0):
    if x >= 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)
def relu(x):
    return max(0, x)

print("EReLU outputs:")

for value in [-4.2, -3.5, -2.8, -2.1, -1.6, -1.0, -0.5, -0.2, 0.0, 0.4, 1.2, 2.5]:
    print(f"Input: {value:5.1f} -> EReLU: {erelu(value):.4f}")
print("\nReLU outputs:")

for value in [-4.2, -3.5, -2.8, -2.1, -1.6, -1.0, -0.5, -0.2, 0.0, 0.4, 1.2, 2.5]:
    print(f"Input: {value:5.1f} -> ReLU: {relu(value):.4f}")