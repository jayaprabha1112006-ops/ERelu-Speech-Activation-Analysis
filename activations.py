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
negative_values = [x for x in speech_features if x < 0]

print("\nNegative Activation Analysis:")
print(f"Total input values: {len(speech_features)}")
print(f"Negative input values: {len(negative_values)}")
print(
    f"Percentage of negative values: "
    f"{len(negative_values) / len(speech_features) * 100:.2f}%"
)

print("\nBehavior for negative inputs:")

for value in negative_values:
    print(
        f"Input: {value:5.1f} | "
        f"EReLU: {erelu(value):7.4f} | "
        f"ReLU: {relu(value):7.4f} | "
        f"Leaky ReLU: {leaky_relu(value):7.4f}"
    )