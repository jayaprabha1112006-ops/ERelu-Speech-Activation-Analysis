import matplotlib.pyplot as plt

from activations import erelu, relu, leaky_relu


# Generate input values
inputs = [x / 10 for x in range(-50, 31)]

# Calculate activation outputs
erelu_outputs = [erelu(x) for x in inputs]
relu_outputs = [relu(x) for x in inputs]
leaky_relu_outputs = [leaky_relu(x) for x in inputs]


# Plot EReLU
plt.plot(inputs, erelu_outputs, label="EReLU")

# Plot ReLU
plt.plot(inputs, relu_outputs, label="ReLU")

# Plot Leaky ReLU
plt.plot(inputs, leaky_relu_outputs, label="Leaky ReLU")

plt.axhline(0)
plt.axvline(0)

plt.xlabel("Input Activation")
plt.ylabel("Output")
plt.title("Comparison of Activation Functions")

plt.legend()
plt.grid(True)

plt.savefig("activation_comparison.png")
plt.show()