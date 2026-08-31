from speech_features import speech_features
from activations import erelu, relu, leaky_relu


negative_values = [x for x in speech_features if x < 0]
erelu_preserved = sum(erelu(x) < 0 for x in negative_values)
relu_preserved = sum(relu(x) < 0 for x in negative_values)
leaky_relu_preserved = sum(leaky_relu(x) < 0 for x in negative_values)


print("\n------------------------------------Negative Feature Preservation---------------------------------------")
print(f"Negative input features: {len(negative_values)}")
print(f"EReLU preserves: {erelu_preserved}")
print(f"ReLU preserves: {relu_preserved}")
print(f"Leaky ReLU preserves: {leaky_relu_preserved}\n")

print("---------------------------------------Interpretation-------------------------------------------------\n")
print(
    "EReLU : It preserves negative activation information while "
    "compressing negative values into a bounded range.\n"
)

print(
    "ReLU : It converts all negative activations to zero, "
    "which removes their sign and magnitude information.\n"
)

print(
    "Leaky ReLU : It preserves negative activations but scales "
    "them by a small factor.\n"
)
