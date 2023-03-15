import numpy as np
import matplotlib.pyplot as plt

# Define the probabilities
P = {'A': 0.1, 'B': 0.2, 'C': 0.2, 'D': 0.2, 'E': 0.3}

# Sort the probabilities in ascending order
sorted_P = sorted(P.items(), key=lambda x: x[1])

# Initialize the Huffman tree
tree = [[sorted_P.pop(0)], [sorted_P.pop(0)]]

# Build the Huffman tree
while len(sorted_P) > 0:
    freq = sorted_P.pop(0)
    node = [freq]
    if freq[1] <= tree[0][0][1]:
        tree.insert(0, node)
    else:
        tree.append(node)
    if len(tree) > 2:
        if tree[0][0][1] < tree[1][0][1]:
            tree[0], tree[1] = tree[1], tree[0]
        merged_node = [tree.pop(0), tree.pop(0)]
        merged_freq = (merged_node[0][0][1] + merged_node[1][0][1])
        merged_node.insert(0, ('', merged_freq))
        if merged_freq <= tree[0][0][1]:
            tree.insert(0, merged_node)
        else:
            tree.append(merged_node)

# Traverse the Huffman tree to get the binary code for each symbol
def traverse(node, code=''):
    if len(node) == 3:
        traverse(node[1], code + '0')
        traverse(node[2], code + '1')
    else:
        codes[node[0][0]] = code

# Generate the binary codes for each symbol
codes = {}
traverse(tree[0])
    
# Plot the Huffman tree and display the binary codes
fig, ax = plt.subplots(figsize=(8, 5))

def plot_tree(node, x=0, y=0, dx=1, dy=1):
    if len(node) == 3:
        x_left = plot_tree(node[1], x, y - dy, dx/2, dy)
        x_right = plot_tree(node[2], x + dx/2, y - dy, dx/2, dy)
        ax.plot([x, x_left + dx/2, x_right], [y, y - dy, y - dy], 'k')
        return x_left + dx
    else:
        ax.text(x + dx/2, y, node[0][0], ha='center', va='center', fontsize=12)
        ax.text(x + dx/2, y - dy, codes[node[0][0]], ha='center', va='top', fontsize=12)
        return x

plot_tree(tree[0], dx=1.5, dy=0.5)
ax.set_xlim([-0.5, len(codes)-0.5])
ax.set_ylim([-2, 0.5])
ax.axis('off')
plt.show()

# Print the binary codes for each symbol
print(codes)
